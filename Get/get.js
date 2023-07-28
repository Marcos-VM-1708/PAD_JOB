from scrapfly import ScrapflyClient, ScrapeConfig

scrapfly = ScrapflyClient(key="YOUR_SCRAPFLY_KEY", max_concurrency=2)

script = 'return document.querySelector("h1").innerHTML'  # get first header text
result = scrapfly.scrape(
    ScrapeConfig(
        url="https://httpbin.org/html",
        # enable javascript rendering for this request and execute a script:
        render_js=True,
        js=script,
    )
)
# results are located in the browser_data field:
title = result.scrape_result['browser_data']['javascript_evaluation_result']
print(title)