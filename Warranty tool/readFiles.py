import xml.etree.ElementTree as ET
from numpy import empty
import pandas as pd
import datetime as dt


from pandas import DataFrame, concat


# # print(root.tag)
# # with open("C:\ILVA461P.001", "r", encoding='UTF-8') as file:
# # print(file.read())


def newDate(oldDate):  # correct date format for excel spreadsheet (according to GAP instructions)
    return (dt.datetime.strptime(f'{oldDate}', '%Y-%M-%d').strftime('%d.%M.%Y'))


def correctFinance(insert):  # corrects amounts in excel, double digts
    toFloat = format(float(insert.text), '.2f').replace('.', ',')
    return toFloat


# in each claim tag necessary data is collected and added as a new key with value
def readFiles(location):
    tree = ET.parse(location)
    root = tree.getroot()
    claimList = []
    cD = dt.datetime.now()
    for a in root.iter('claim'):
        done = {}
        for i in a.iter('dc_importer_no'):
            done['importer'] = i.text
        for dealer in a.iter('dealer_no'):
            done['dealer'] = dealer.text
        for order_no in a.iter('repair_order_no'):
            done['order_no'] = order_no.text
        for vin in a.iter('vin'):
            done['vin'] = vin.attrib['vin']
        for sales_model in a.iter('sales_model'):
            done['sales_model'] = sales_model.attrib['sales_model']
        for km in a.iter('kilometres'):
            done['km'] = km.text
        for version in a.iter('version'):
            done['version'] = version.text
        for service_no in a.iter('service_no'):
            done['service_no'] = service_no.text
        for manufacturer_removed_part in a.iter('manufacturer_removed_part'):
            done['manufacturer_removed_part'] = manufacturer_removed_part.text
        for type_of_damage in a.iter('type_of_damage'):
            done['type_of_damage'] = type_of_damage.text
        for claim_type_partner in a.iter('claim_type_partner'):
            readyType = ''
            for claimType in claim_type_partner:
                readyType += claimType.text
            done['dealer_claim_type_code'] = readyType
        for repair_code in a.iter('repair_code'):
            done['repair_code'] = repair_code.text
        for production_date in a.iter('production_date'):
            done['production_date'] = newDate(production_date.text)
        for delivery_date in a.iter('delivery_date'):
            done['delivery_date'] = newDate(delivery_date.text)
        for repair_date in a.iter('repair_date'):
            done['repair_date'] = newDate(repair_date.text)
        done['buchdat'] = cD.strftime('%d.%m.%Y')
        for loss in a.iter('loss'):
            if(loss.text == '+1'):
                done['loss'] = loss.text[1]
            else:
                done['loss'] = loss.text
        for total_time_units_partner in a.iter('total_time_units_partner'):
            done['total_time_units_partner'] = total_time_units_partner.text
        for tl_deal_deal_cur in a.iter('tl_deal_deal_cur'):
            done['tl_deal_deal_cur'] = correctFinance(tl_deal_deal_cur)
        for tol_deal_deal_cur in a.iter('tol_deal_deal_cur'):
            done['tol_deal_deal_cur'] = correctFinance(tol_deal_deal_cur)
        for tm_price_deal_deal_cur in a.iter('tm_price_deal_deal_cur'):
            done['tm_price_deal_deal_cur'] = correctFinance(
                tm_price_deal_deal_cur)
        for tom_deal_deal_cur in a.iter('tom_deal_deal_cur'):
            done['tom_deal_deal_cur'] = correctFinance(tom_deal_deal_cur)
        for tcv_deal_deal_cur in a.iter('tcv_deal_deal_cur'):
            done['tcv_deal_deal_cur'] = correctFinance(tcv_deal_deal_cur)
        for claim_serial_no in a.iter('claim_serial_no'):
            done['claim_serial_no'] = claim_serial_no.text
        for order_receipt_date in a.iter('order_receipt_date'):
            done['order_receipt_date'] = newDate(order_receipt_date.text)
        for no_denoting_duty_to_report in a.iter('no_denoting_duty_to_report'):
            done['no_denoting_duty_to_report'] = no_denoting_duty_to_report.text
        for make in a.iter('make'):
            done['make'] = make.text
        for paying_production_subsidiary in a.iter('paying_production_subsidiary'):
            done['paying_production_subsidiary'] = paying_production_subsidiary.text
        for importer_currency in a.iter('importer_currency'):
            done['importer_currency'] = importer_currency.textnpm
        for claim_date in a.iter('claim_date'):
            done['claim_date'] = newDate(claim_date.text)

        claimList.append(done)

    df = DataFrame(data=claimList)
    writer = pd.ExcelWriter(
        f'GAP{cD.day * 10000000000 + cD.month * 100000000 + cD.year * 10000 + cD.hour * 100 + cD.minute * 1 }.xlsx', engine="xlsxwriter")
    df.to_excel(writer, index=False, header=False, float_format='%.2f')
    writer.save()
    print('Excel saved')
