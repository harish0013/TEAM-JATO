# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
#
# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
#
#
# class AutoscoutPipeline:
#     def process_item(self, item, spider):
#         return item


# autoscout/pipelines.py

# autoscout/pipelines.py

import csv

class VehicleDetailsPipeline:
    def open_spider(self, spider):
        self.file = open('vehicle_details.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        self.writer.writerow([
            'Make', 'Model', 'Trim', 'Derivative', 'DerivativeTranslatedEnglish', 'Powertrain', 'VersionName',
            'VersionNameTranslatedEnglish', 'Currency', 'Price', 'DeliveryCost', 'Country', 'Date', 'CustomerType',
            'MonthlyPaymentType', 'ProductName', 'MonthlyPaymentProviderName', 'MonthlyPaymentProviderType',
            'ContractDuration', 'YearlyMileageKm', 'YearlyMileageMiles', 'TotalContractMileageKm',
            'TotalContractMileageMiles', 'DepositRetail', 'DepositPercentOfPrice', 'MonthlyPaymentEMI', 'DataSource',
            'URL', 'OtherSource', 'VehiclePriceReference', 'NumberOfDoors','bodyType','builtoption','productdescription'
        ])

    def process_item(self, item, spider):
        self.writer.writerow([
            item.get('Make'), item.get('Model'), item.get('Trim'), item.get('Derivative'),
            item.get('DerivativeTranslatedEnglish'), item.get('Powertrain'), item.get('VersionName'),
            item.get('VersionNameTranslatedEnglish'), item.get('Currency'), item.get('Price'), item.get('DeliveryCost'),
            item.get('Country'), item.get('Date'), item.get('CustomerType'), item.get('MonthlyPaymentType'),
            item.get('ProductName'), item.get('MonthlyPaymentProviderName'),
            item.get('MonthlyPaymentProviderType'), item.get('ContractDuration'), item.get('YearlyMileageKm'),
            item.get('YearlyMileageMiles'), item.get('TotalContractMileageKm'),
            item.get('TotalContractMileageMiles'), item.get('DepositRetail'), item.get('DepositPercentOfPrice'),
            item.get('MonthlyPaymentEMI'), item.get('DataSource'), item.get('URL'), item.get('OtherSource'),
            item.get('VehiclePriceReference'), item.get('NumberOfDoors'),item.get('bodyType'),item.get('builtoption'),item.get('productdescription')
        ])
        return item

    def close_spider(self, spider):
        self.file.close()
