import random
from utils import visual_utils
from tqdm import tqdm
from selenium.webdriver.common.by import By

# types
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


def get_random_rgb_string():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_str = f"rgb({r},{g},{b})"
    return rgb_str


def generate_transparent_color_from_rgb_string(rgb_str):
    rgb_str = rgb_str[:-1]
    rgb_str += ",0.3)"
    return rgb_str


def is_in_viewport(driver: WebDriver, element: WebElement):
    is_in_viewport_js = """
	function isElementInViewport(el) {
		var bounding = el.getBoundingClientRect();
		return (
			bounding.top >= 0 &&
			bounding.left >= 0 &&
			bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
			bounding.right <= (window.innerWidth || document.documentElement.clientWidth)
		);
	}
	return isElementInViewport(arguments[0]);
	"""

    driver.execute_script(is_in_viewport_js, is_in_viewport_js)


def is_element_size_valid(element: WebElement, verbose = False):
    size = element.size
    if size["width"] == 0 or size["height"] == 0:
        if verbose:
            print(f"Invalid {element.tag_name} size found.") 
        return False
    return True


def paint_border(
    driver: WebDriver,
    element: WebElement,
    borderColor="tomato",
    backgroundColor="rgba(255, 0, 0, 0.5)",
):
    driver.execute_script(
        f"paintBorderAsNewDiv(arguments[0], arguments[1], arguments[2])",
        element,
        borderColor,
        backgroundColor,
    )


def paint_corner_labels(driver: WebDriver, element: WebElement, color="tomato)"):
    # If either width or weight == 0, skip
    size = element.size

    # Paint corner labels
    location = element.location
    corners = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for corner in corners:
        posX = location["x"] + (size["width"] * corner[0])
        posY = location["y"] + (size["height"] * corner[1])
        driver.execute_script(f"paintCornerLabels({posX},{posY},'{color}')")


def draw_annotations(driver: WebDriver, target_tags):
    for tag in target_tags:
        elements = driver.find_elements(By.TAG_NAME, tag)
        color = visual_utils.get_random_rgb_string()
        transparent_color = visual_utils.generate_transparent_color_from_rgb_string(
            color
        )
        for element in tqdm(elements, desc=f"Processing {tag} tags"):
            if is_element_size_valid(element) == False:
                continue

            paint_border(element, borderColor=color, backgroundColor=transparent_color)
            paint_corner_labels(element, color)


def hide_scrollbar(driver: WebDriver):
    driver.execute_script("document.body.style.overflow = 'hidden';")