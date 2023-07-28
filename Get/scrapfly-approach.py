
import json
from scrapfly import ScrapflyClient, ScrapeConfig
from get import script

urls = ["https://goo.gl/maps/Zqzfq43hrRPmWGVB7"]


def parse_place(selector):
    """parse Google Maps place"""

    def aria_with_label(label):
        """gets aria element as is"""
        return selector.css(f"*[aria-label*='{label}']::attr(aria-label)")

    def aria_no_label(label):
        """gets aria element as text with label stripped off"""
        text = aria_with_label(label).get("")
        return text.split(label, 1)[1].strip()

    result = {
        "name": "".join(selector.css("h1 ::text").getall()).strip(),
        "category": selector.css("button[jsaction='pane.rating.category']::text").get(),
        # most of the data can be extracted through accessibility labels:
        "address": aria_no_label("Address: "),
        "website": aria_no_label("Website: "),
        "phone": aria_no_label("Phone: "),
        "review_count": aria_with_label(" reviews").get(),
        # to extract star numbers from text we can use regex pattern for numbers: "\d+"
        "stars": aria_with_label(" stars").re("\d+.*\d+")[0],
        "5_stars": aria_with_label("5 stars").re(r"(\d+) review")[0],
        "4_stars": aria_with_label("4 stars").re(r"(\d+) review")[0],
        "3_stars": aria_with_label("3 stars").re(r"(\d+) review")[0],
        "2_stars": aria_with_label("2 stars").re(r"(\d+) review")[0],
        "1_stars": aria_with_label("1 stars").re(r"(\d+) review")[0],
    }
    return result


scrapfly = ScrapflyClient(key = "YOUR_SCRAPFLY_KEY", max_concurrency = 2)
places = []
for url in urls:
    result = scrapfly.scrape(
        ScrapeConfig(
            url = "https://www.google.com/maps/search/koh+tao+divers+in+koh+tao+thailand/",
            render_js = True,
            js = script,
            country = "US",
        )
    )
    places.append(parse_place(result.selector))
print(json.dumps(places, indent = 2, ensure_ascii = False))