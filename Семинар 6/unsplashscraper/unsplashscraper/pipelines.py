import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import CsvItemExporter

class CustomImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_name = request.meta['image_name']
        return f'{image_name}.jpg'

    def get_media_requests(self, item, info):
        request = scrapy.Request(item['image_url'])
        request.meta['image_name'] = item['image_name']
        return request

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if image_path:
            item['image_path'] = image_path[0]
        return item

class CsvPipeline:
    def open_spider(self, spider):
        self.file = open('images_data.csv', 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = ['image_name', 'category', 'image_url', 'image_path']
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item