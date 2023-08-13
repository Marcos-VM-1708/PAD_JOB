from selenium import webdriver


script = """
function waitCss(selector, n=1, require=false, timeout=5000) {
  console.log(selector, n, require, timeout);
  var start = Date.now();
  while (Date.now() - start < timeout){
  	if (document.querySelectorAll(selector).length >= n){
      return document.querySelectorAll(selector);
    }
  }
  if (require){
      throw new Error(`selector "${selector}" timed out in ${Date.now() - start} ms`);
  } else {
      return document.querySelectorAll(selector);
  }
}

var results = waitCss("div[role*=article]>a", n=10, require=false);
return Array.from(results).map((el) => el.getAttribute("href"))
"""

driver = webdriver.Chrome()


def search(query):
    url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}/?hl=en"
    driver.get(url)
    urls = driver.execute_script(script)
    return urls or [url]


print(f'single search: {search("louvre museum in paris")}')
print(f'multi search: {search("mcdonalds in paris")}')