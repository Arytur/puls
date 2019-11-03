from datetime import date
from app.models import PriceHistory, ProductInShop


class ShopingPipeline(object):
    def process_item(self, item, spider):
        try:
            # check if Product exists
            product_in_shop = ProductInShop.objects.get(url=item['url'])
            # check if price for today already exists
            td = date.today()
            product_in_shop.pricehistory_set.get(updated_at=td)

            # if all tests passed, quit
            return item

        except ProductInShop.DoesNotExist:
            # no product, do nothing
            return

        except PriceHistory.DoesNotExist:
            # continue and save the price for today
            pass

        price_history = PriceHistory()
        price_history.product_in_shop = product_in_shop
        price_history.price = float(item['price'])
        price_history.save()
        return item
