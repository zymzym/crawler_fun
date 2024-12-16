import json 
import requests

def post_html(url, params):
    response = requests.post(url, json=params)
    results = json.loads(response.text)['results'][0]['hits']
    images_list = [i['image'] for i in results]
    return images_list

def get_images(url, params):
    images_list = post_html(url, params)
    for i in range(len(images_list)):
        image_data = requests.get(images_list[i]).content
        with open(f'images/{i}.jpg', 'wb') as f:
            f.write(image_data)

url = 'https://m8gudcg05z-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.17.0)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.56.0)%3B%20Shopify%20Integration%3B%20JS%20Helper%20(3.13.0)&x-algolia-api-key=be523f445a1ebccb9b517c427d86b856&x-algolia-application-id=M8GUDCG05Z'
params = {"requests":[{"indexName":"nudeprodau_products","params":"analyticsTags=%5B%22desktop%22%5D&clickAnalytics=true&distinct=true&facetingAfterDistinct=false&facets=%5B%22meta.product.back_in_stock%22%2C%22meta.product.back_in_stock_unix%22%2C%22meta.product.new%22%2C%22meta.product.publication_date_unix%22%2C%22options.value%22%2C%22options.colour%22%2C%22named_tags.__label%22%2C%22named_tags.pfs%22%2C%22named_tags.CODE%22%2C%22product_type%22%2C%22tags%22%2C%22named_tags.SALE%22%2C%22named_tags.LOWSTOCK%22%2C%22meta.variant.oos_variant%22%2C%22meta.product.first_image%22%2C%22named_tags.lvl0%22%2C%22named_tags.lvl1%22%2C%22named_tags.lvl2%22%2C%22named_tags.lvl3%22%2C%22price%22%2C%22price_range%22%2C%22meta.product.colour_group_erp%22%2C%22options.size%22%2C%22vendor%22%5D&filters=collections%3A%22all-products%22%20AND%20NOT%20tags%3Aalgolia30days&highlightPostTag=__%2Fais-highlight__&highlightPreTag=__ais-highlight__&hitsPerPage=12&maxValuesPerFacet=200&page=0&query=&ruleContexts=%5B%22all-products%22%5D&tagFilters="}]}

get_images(url, params)