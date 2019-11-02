from datetime import date
from app.models import PriceHistory, Product


class ShopingPipeline(object):
    def process_item(self, item, spider):
        try:
            # check if Product exists
            product = Product.objects.get(productinshop__url=item['url'])
            # check if price for today already exists
            td = date.today()
            product.pricehistory_set.get(date=td)

            # if all tests passed, quit
            return item

        except Product.DoesNotExist:
            # no product, do nothing
            return

        except PriceHistory.DoesNotExist:
            # continue and save the price for today
            pass

        price_history = PriceHistory()
        price_history.product = product
        price_history.price = float(item['price'])
        price_history.save()
        return item
