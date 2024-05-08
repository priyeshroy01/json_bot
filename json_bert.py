import logging
import sys
import os
import openai
from IPython.display import Markdown, display
from llama_index.llms.openai import OpenAI
from llama_index.core.indices.struct_store import JSONQueryEngine
import streamlit as st

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
os.environ["OPENAI_API_KEY"] = "sk-proj-dDu3AWI1Keq4UZwxfKDrT3BlbkFJ71rGMYpzBJhdZa14x0dO"


# Test on some sample data
json_value = {
    "Header": {
        "SalesOrg": "1000",
        "Trademark": "01",
        "SalesOrderNumber": "9237448",
        "OrderType": "ZSTD",
        "SalesDocumentVersionNumber": "4.43.1068",
        "SalesOfficeNumber": "851",
        "OrderDate": "2024-03-25T00:00:00",
        "JobName": "MDA-Peleton FSI Warehouse",
        "PurchaseOrderNumber": "5032407100201",
        "CustomerPurchaseOrderNumber": "null",
        "SalesPersonId": "11527",
        "SalesPersonName": "Chuck Barlage",
        "SalesPersonEmail": "chuck@aircontrolproducts.com",
        "Z5PartnerNumber": "null",
        "Incoterms": "P",
        "OrderTotal": 185575.64,
        "Currency": "USD",
        "PricingProcedure": "ZGFC3",
        "InternationalOrder": "false",
        "CustomerReference": "null",
        "AtuOrder": "N"
    },
    
    "Partners": [
        {
            "PartnerId": "850",
            "PartnerType": "BILL_TO",
            "Name": "AIR CONTROL PRODUCTS INC",
            "Company": "null",
            "AddressLine1": "3800 TOWPATH RD",
            "AddressLine2": "null",
            "AddressLine3": "null",
            "AddressLine4": "null",
            "Country": "US",
            "State": "OH",
            "City": "BROADVIEW HEIGHTS",
            "Zip": "44147",
            "Fax": "4405260503",
            "Phone": "4405263020",
            "Email": "null"
        },
        {
            "PartnerId": "62014",
            "PartnerType": "CONTACT",
            "Name": "Chuck Barlage",
            "Company": "null",
            "AddressLine1": "2164 TEDROW RD",
            "AddressLine2": "null",
            "AddressLine3": "null",
            "AddressLine4": "null",
            "Country": "US",
            "State": "OH",
            "City": "TOLEDO",
            "Zip": "43614",
            "Fax": "14193808998",
            "Phone": "4193808990",
            "Email": "chuck@aircontrolproducts.com"
        },
        {
            "PartnerId": "850",
            "PartnerType": "PAYER",
            "Name": "AIR CONTROL PRODUCTS INC",
            "Company": "null",
            "AddressLine1": "3800 TOWPATH RD",
            "AddressLine2": "null",
            "AddressLine3": "null",
            "AddressLine4": "null",
            "Country": "US",
            "State": "OH",
            "City": "BROADVIEW HEIGHTS",
            "Zip": "44147",
            "Fax": "4405260503",
            "Phone": "4405263020",
            "Email": "null"
        },
        {
            "PartnerId": "851",
            "PartnerType": "SHIP_TO",
            "Name": "First Solar",
            "Company": "C/O Program Solutions Group",
            "AddressLine1": "10 Eastwood Drive",
            "AddressLine2": "null",
            "AddressLine3": "null",
            "AddressLine4": "null",
            "Country": "US",
            "State": "OH",
            "City": "Luckey",
            "Zip": "43443",
            "Fax": "null",
            "Phone": "(419)699-1047",
            "Email": "null"
        },
        {
            "PartnerId": "851",
            "PartnerType": "SOLD_TO",
            "Name": "AIR CONTROL PRODUCTS INC",
            "Company": "null",
            "AddressLine1": "2164 TEDROW RD",
            "AddressLine2": "null",
            "AddressLine3": "null",
            "AddressLine4": "null",
            "Country": "US",
            "State": "OH",
            "City": "TOLEDO",
            "Zip": "43614",
            "Fax": "14193808998",
            "Phone": "4193808990",
            "Email": "null"
        }
    ],
    "Notes": [
        {
            "NoteTypeCode": "CUST_MSG",
            "NoteTypeDescription": "Must Notify to Customer Message",
            "Note": "Delivery Appt Required. Notify Jason Mason at 419-944-1728 or phil@aircontrolproducts.com  or Alternative Number 419-699-1047 - 24  Hours Prior To Delivery."
        }
    ],
    "DeliveryGroups": [
        {
            "DeliveryGroupNumber": "1",
            "DeliveryPriority": "99",
            "DeliveryPriorityDescription": "STD",
            "MessageText": "null",
            "OverallStatus": "SCHEDULED",
            "HoldStatus": "null",
            "PromiseDate": "2024-06-19T00:00:00",
            "RepromiseDate": "null",
            "OverallStatusAdditionalText": "null",
            "Lines": [
                {
                    "SalesOrderLineNumber": "190",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "RDU-48",
                    "ShortModelName": "null",
                    "OrderedQuantity": 27.000,
                    "ItemCategory": "ZLLV",
                    "ProductClass": "2H",
                    "Mark": "RF-1",
                    "Material": "RDU-48",
                    "MaterialDescription": "ROOFTOP UPBLAST PROP DIRECT",
                    "PlantDescription": "WI Mfg Fac 2 Schof (AXL/INLNE)",
                    "Division": "11",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "11RU",
                    "PlantNumber": "1050",
                    "HigherLevelSalesOrderLine": "180",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV5",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0002",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0003",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0004",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0005",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0006",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0007",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0008",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0009",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0010",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0011",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0012",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0013",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0014",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0015",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0016",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0017",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0018",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0019",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0020",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0021",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0022",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0023",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0024",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0025",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0026",
                            "TagName": "RF-1"
                        },
                        {
                            "Tag": "0027",
                            "TagName": "RF-1"
                        }
                    ],
                    "Multiplier": 0.4482,
                    "TotalListPrice": 261117.00,
                    "TotalNetPrice": 117032.64,
                    "TotalBillingPrice": 117032.64,
                    "TotalDiscountPrice": 144084.36
                }
            ],
            "Shipments": []
        },
        {
            "DeliveryGroupNumber": "2",
            "DeliveryPriority": "99",
            "DeliveryPriorityDescription": "STD",
            "MessageText": "null",
            "OverallStatus": "COMPLETE",
            "HoldStatus": "null",
            "PromiseDate": "2024-04-10T00:00:00",
            "RepromiseDate": "null",
            "OverallStatusAdditionalText": "null",
            "Lines": [
                {
                    "SalesOrderLineNumber": "220",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "VCD-23-48X48",
                    "ShortModelName": "null",
                    "OrderedQuantity": 12.000,
                    "ItemCategory": "ZLLV",
                    "ProductClass": "D0",
                    "Mark": "SF-1",
                    "Material": "VCD-23",
                    "MaterialDescription": "CNTRL DMPR",
                    "PlantDescription": "OK Mfg B#400 Tulsa (DMPR)",
                    "Division": "60",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "2024-04-10T00:00:00",
                    "ProcessingStatus": "C",
                    "MaterialGroup": "60CA",
                    "PlantNumber": "2100",
                    "HigherLevelSalesOrderLine": "200",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV5",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0002",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0003",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0004",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0005",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0006",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0007",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0008",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0009",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0010",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0011",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0012",
                            "TagName": "SF-1"
                        }
                    ],
                    "Multiplier": 0.4482,
                    "TotalListPrice": 19944.00,
                    "TotalNetPrice": 8938.90,
                    "TotalBillingPrice": 8938.90,
                    "TotalDiscountPrice": 11005.10
                }
            ],
            "Shipments": [
                {
                    "OutboundNumber": "84845565",
                    "ShipmentNumber": "5110630",
                    "DeliveryGroupNumber": "2",
                    "GoodsIssueDate": "2024-04-10T00:00:00",
                    "CarrierCode": "CNWY",
                    "CarrierName": "XPO LOGISTICS LTL",
                    "CarrierUrl": "https://app.ltl.xpo.com/appjs/tracking/details/{0}",
                    "CarrierScacCode": "null",
                    "OutboundCreationDate": "2024-04-08T00:00:00",
                    "ShipmentType": "ZLTL",
                    "ShipmentTypeDescription": "LTL SHIPMENT",
                    "EquipmentTypeCode": "01",
                    "EquipmentTypeDescription": "Truck",
                    "ShippingPlant": "2100",
                    "ShippingPlantDescription": "OK Mfg B#400 Tulsa (DMPR)",
                    "EchoShippingAccountNumber": "E116680",
                    "ForwardingAgent": "CNWY",
                    "ForwardingAgentTrackingId": "null",
                    "ShipmentTrackingNumber": "408067962",
                    "LoadOnDate": "2024-04-10T00:00:00",
                    "ShipmentDescription": "OK Mfg B#400 Tulsa (DMPR)",
                    "ExternalIdentification1": "408067962",
                    "ExternalIdentification2": "57789505",
                    "ShipmentText": "null",
                    "ShipmentStatus": "DEPARTED",
                    "EstimatedDeliveryDate": "null",
                    "DepartedDate": "2024-04-10T00:00:00",
                    "LoadIndicator": "- Non-optimized",
                    "Lines": [
                        {
                            "SalesOrderLineNumber": "220",
                            "ShippedQuantity": 12.0
                        }
                    ],
                    "DeliveryNotes": [
                        {
                            "NoteCode": "Shipment delivered",
                            "NoteDesc": "Delivered : Stop 2 updated Departure from 4/15 07:51 to 4/15 10:51",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-15T10:51:00"
                        },
                        {
                            "NoteCode": "Delivered",
                            "NoteDesc": "Delivered by Perrysburg, OH",
                            "City": "Lucky",
                            "State": "OH",
                            "Timestamp": "2024-04-15T09:51:00"
                        },
                        {
                            "NoteCode": "Out for Delivery",
                            "NoteDesc": "Out for delivery Perrysburg, OH as of 04/15/2024",
                            "City": "Perrysburg",
                            "State": "OH",
                            "Timestamp": "2024-04-15T08:03:00"
                        },
                        {
                            "NoteCode": "Shipment delivered",
                            "NoteDesc": "EDI Status: Shipment Delivered",
                            "City": "Perrysburg",
                            "State": "OH",
                            "Timestamp": "2024-04-15T07:51:00"
                        },
                        {
                            "NoteCode": "Out for Delivery",
                            "NoteDesc": "EDI Status: Tendered for Delivery",
                            "City": "Perrysburg",
                            "State": "OH",
                            "Timestamp": "2024-04-15T06:03:00"
                        },
                        {
                            "NoteCode": "Shipment Notification",
                            "NoteDesc": "At destination Perrysburg, OH Last update as of 05:03 AM On 04/15/2024",
                            "City": "Perrysburg",
                            "State": "OH",
                            "Timestamp": "2024-04-15T04:03:00"
                        },
                        {
                            "NoteCode": "Shipment enroute",
                            "NoteDesc": "EDI Status: Arrived at Terminal Location",
                            "City": "Perrysburg",
                            "State": "OH",
                            "Timestamp": "2024-04-15T01:20:00"
                        },
                        {
                            "NoteCode": "Shipment enroute",
                            "NoteDesc": "En route to destination Perrysburg, OH",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-14T13:07:00"
                        },
                        {
                            "NoteCode": "Shipment enroute",
                            "NoteDesc": "EDI Status: Departed Terminal Location",
                            "City": "Plainfield",
                            "State": "IN",
                            "Timestamp": "2024-04-14T11:07:00"
                        },
                        {
                            "NoteCode": "Shipment Notification",
                            "NoteDesc": "Waiting for Carrier Update",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-14T04:20:00"
                        },
                        {
                            "NoteCode": "Shipment Notification",
                            "NoteDesc": "At interim Plainfield, IN Last update as of 04:16 AM On 04/13/2024",
                            "City": "Plainfield",
                            "State": "IN",
                            "Timestamp": "2024-04-13T03:16:00"
                        },
                        {
                            "NoteCode": "Shipment Notification",
                            "NoteDesc": "At interim Plainfield, IN Last update as of 12:57 AM On 04/13/2024",
                            "City": "Plainfield",
                            "State": "IN",
                            "Timestamp": "2024-04-12T23:57:00"
                        },
                        {
                            "NoteCode": "Shipment enroute",
                            "NoteDesc": "EDI Status: Arrived at Terminal Location",
                            "City": "Plainfield",
                            "State": "IN",
                            "Timestamp": "2024-04-12T21:22:00"
                        },
                        {
                            "NoteCode": "Shipment enroute",
                            "NoteDesc": "En route to interim Plainfield, IN",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-12T19:36:00"
                        },
                        {
                            "NoteCode": "Shipment Notification",
                            "NoteDesc": "Waiting for Carrier Update",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-12T19:20:00"
                        },
                        {
                            "NoteCode": "Shipment enroute",
                            "NoteDesc": "EDI Status: Departed Terminal Location",
                            "City": "Saint Louis",
                            "State": "MO",
                            "Timestamp": "2024-04-12T17:36:00"
                        },
                        {
                            "NoteCode": "Shipment enroute",
                            "NoteDesc": "\nPer carrier website: The shipment is in transit. ETA. \n04/16",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-12T15:45:00"
                        },
                        {
                            "NoteCode": "Shipment Notification",
                            "NoteDesc": "Arrived at interim Saint Louis, MO At 05:58 AM On 04/12/2024",
                            "City": "Saint Louis",
                            "State": "MO",
                            "Timestamp": "2024-04-12T05:58:00"
                        },
                        {
                            "NoteCode": "Shipment enroute",
                            "NoteDesc": "En route to interim Saint Louis, MO",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-12T02:42:00"
                        },
                        {
                            "NoteCode": "Shipment Notification",
                            "NoteDesc": "At interim Marshfield, MO Last update as of 02:27 AM On 04/12/2024",
                            "City": "Marshfield",
                            "State": "MO",
                            "Timestamp": "2024-04-12T02:27:00"
                        },
                        {
                            "NoteCode": "Picked Up",
                            "NoteDesc": "Picked Up : Stop 1 updated Departure from 1/1 02:09 to 4/12 02:00",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-12T02:00:00"
                        },
                        {
                            "NoteCode": "Shipment Notification",
                            "NoteDesc": "Recorded in system Marshfield, MO as of 04/12/2024",
                            "City": "Marshfield",
                            "State": "MO",
                            "Timestamp": "2024-04-12T01:33:00"
                        },
                        {
                            "NoteCode": "Shipment Loaded",
                            "NoteDesc": "EDI Status: Departed Pickup Location",
                            "City": "TULSA",
                            "State": "OK",
                            "Timestamp": "2024-04-12T00:00:00"
                        },
                        {
                            "NoteCode": "Shipment enroute",
                            "NoteDesc": "En route to interim Marshfield, MO",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-11T21:20:00"
                        },
                        {
                            "NoteCode": "Shipment Notification",
                            "NoteDesc": "At origin Glenpool, OK as of 04/11/2024",
                            "City": "Glenpool",
                            "State": "OK",
                            "Timestamp": "2024-04-11T18:58:00"
                        },
                        {
                            "NoteCode": "Shipment Exception",
                            "NoteDesc": "Per carrier call((800) 548-8608): Swap trailer, the freight has not been picked up yet.",
                            "City": "",
                            "State": "",
                            "Timestamp": "2024-04-11T15:33:00"
                        }
                    ]
                }
            ]
        },
        {
            "DeliveryGroupNumber": "3",
            "DeliveryPriority": "99",
            "DeliveryPriorityDescription": "STD",
            "MessageText": "null",
            "OverallStatus": "SCHEDULED",
            "HoldStatus": "null",
            "PromiseDate": "2024-05-17T00:00:00",
            "RepromiseDate": "null",
            "OverallStatusAdditionalText": "null",
            "Lines": [
                {
                    "SalesOrderLineNumber": "110",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "G-240-30-VG-1-34-X",
                    "ShortModelName": "null",
                    "OrderedQuantity": 1.000,
                    "ItemCategory": "ZLLV",
                    "ProductClass": "3A",
                    "Mark": "EF-7",
                    "Material": "G-240",
                    "MaterialDescription": "CENTR ROOF EXH FAN",
                    "PlantDescription": "WI Mfg Fac 2 Schof (PRV)",
                    "Division": "13",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "13FJ",
                    "PlantNumber": "1110",
                    "HigherLevelSalesOrderLine": "100",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV1",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-7"
                        }
                    ],
                    "Multiplier": 0.4637,
                    "TotalListPrice": 6494.00,
                    "TotalNetPrice": 3011.27,
                    "TotalBillingPrice": 3011.27,
                    "TotalDiscountPrice": 3482.73
                },
                {
                    "SalesOrderLineNumber": "120",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "387186",
                    "ShortModelName": "null",
                    "OrderedQuantity": 1.000,
                    "ItemCategory": "ZSTK",
                    "ProductClass": "9A",
                    "Mark": "EF-7",
                    "Material": "387186",
                    "MaterialDescription": "VARI-GREEN HOA CONTROL",
                    "PlantDescription": "WI National Distrib Ctr Schof",
                    "Division": "01",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "9XA",
                    "PlantNumber": "1251",
                    "HigherLevelSalesOrderLine": "100",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV1",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-7"
                        }
                    ],
                    "Multiplier": 0.4637,
                    "TotalListPrice": 396.00,
                    "TotalNetPrice": 183.63,
                    "TotalBillingPrice": 183.63,
                    "TotalDiscountPrice": 212.37
                },
                {
                    "SalesOrderLineNumber": "130",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "386367",
                    "ShortModelName": "null",
                    "OrderedQuantity": 1.000,
                    "ItemCategory": "ZSTK",
                    "ProductClass": "null",
                    "Mark": "EF-7",
                    "Material": "386367",
                    "MaterialDescription": "TSTAT,LINE VOLTAGE,COLUMBUS,ET9SRTS",
                    "PlantDescription": "WI National Distrib Ctr Schof",
                    "Division": "01",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "9XA",
                    "PlantNumber": "1251",
                    "HigherLevelSalesOrderLine": "100",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV1",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-7"
                        }
                    ],
                    "Multiplier": 0.4637,
                    "TotalListPrice": 120.00,
                    "TotalNetPrice": 55.64,
                    "TotalBillingPrice": 55.64,
                    "TotalDiscountPrice": 64.36
                },
                {
                    "SalesOrderLineNumber": "140",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "WD100-24X24",
                    "ShortModelName": "null",
                    "OrderedQuantity": 1.000,
                    "ItemCategory": "ZSTK",
                    "ProductClass": "DA",
                    "Mark": "EF-7",
                    "Material": "WD100-24X24",
                    "MaterialDescription": "DMPR",
                    "PlantDescription": "WI Mfg Fac 11 Mosinee (DMPR)",
                    "Division": "60",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "60AB",
                    "PlantNumber": "1100",
                    "HigherLevelSalesOrderLine": "100",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV1",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-7"
                        }
                    ],
                    "Multiplier": 0.4637,
                    "TotalListPrice": 223.00,
                    "TotalNetPrice": 103.41,
                    "TotalBillingPrice": 103.41,
                    "TotalDiscountPrice": 119.59
                },
                {
                    "SalesOrderLineNumber": "160",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "G-095-D-8-1-17-X",
                    "ShortModelName": "null",
                    "OrderedQuantity": 1.000,
                    "ItemCategory": "ZLLV",
                    "ProductClass": "3A",
                    "Mark": "EF-8",
                    "Material": "G-095",
                    "MaterialDescription": "G-095 CENTR ROOF EXH FAN",
                    "PlantDescription": "WI Mfg Fac 2 Schof (PRV)",
                    "Division": "13",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "13CA",
                    "PlantNumber": "1110",
                    "HigherLevelSalesOrderLine": "150",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV7",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-8"
                        }
                    ],
                    "Multiplier": 0.4562,
                    "TotalListPrice": 725.00,
                    "TotalNetPrice": 330.75,
                    "TotalBillingPrice": 330.75,
                    "TotalDiscountPrice": 394.25
                },
                {
                    "SalesOrderLineNumber": "170",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "BD100-10X10",
                    "ShortModelName": "null",
                    "OrderedQuantity": 1.000,
                    "ItemCategory": "ZSTK",
                    "ProductClass": "D10",
                    "Mark": "EF-8",
                    "Material": "BD100-10X10",
                    "MaterialDescription": "DMPR,BD100-10X10",
                    "PlantDescription": "WI Mfg Fac 11 Mosinee (DMPR)",
                    "Division": "60",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "60AC",
                    "PlantNumber": "1100",
                    "HigherLevelSalesOrderLine": "150",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV7",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-8"
                        }
                    ],
                    "Multiplier": 0.4562,
                    "TotalListPrice": 81.00,
                    "TotalNetPrice": 36.95,
                    "TotalBillingPrice": 36.95,
                    "TotalDiscountPrice": 44.05
                },
                {
                    "SalesOrderLineNumber": "20",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "GB-100-4-1-19-X",
                    "ShortModelName": "null",
                    "OrderedQuantity": 1.000,
                    "ItemCategory": "ZLLV",
                    "ProductClass": "4A",
                    "Mark": "EF-1",
                    "Material": "GB-101",
                    "MaterialDescription": "GB-101 CENTR ROOF EXH FAN",
                    "PlantDescription": "WI Mfg Fac 2 Schof (PRV)",
                    "Division": "13",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "13BB",
                    "PlantNumber": "1110",
                    "HigherLevelSalesOrderLine": "10",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV7",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-1"
                        }
                    ],
                    "Multiplier": 0.4562,
                    "TotalListPrice": 1204.00,
                    "TotalNetPrice": 549.26,
                    "TotalBillingPrice": 549.26,
                    "TotalDiscountPrice": 654.74
                },
                {
                    "SalesOrderLineNumber": "210",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "RBF-3H48-75",
                    "ShortModelName": "null",
                    "OrderedQuantity": 12.000,
                    "ItemCategory": "ZLLV",
                    "ProductClass": "2E",
                    "Mark": "SF-1",
                    "Material": "RBF-3H48",
                    "MaterialDescription": "ROOF PROP FAN",
                    "PlantDescription": "WI Mfg Fac 2 Schof (AXL/INLNE)",
                    "Division": "11",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "11AA",
                    "PlantNumber": "1050",
                    "HigherLevelSalesOrderLine": "200",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV5",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0002",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0003",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0004",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0005",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0006",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0007",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0008",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0009",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0010",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0011",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0012",
                            "TagName": "SF-1"
                        }
                    ],
                    "Multiplier": 0.4482,
                    "TotalListPrice": 78132.00,
                    "TotalNetPrice": 35018.76,
                    "TotalBillingPrice": 35018.76,
                    "TotalDiscountPrice": 43113.24
                },
                {
                    "SalesOrderLineNumber": "230",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "RBF-3H48-HOOD",
                    "ShortModelName": "null",
                    "OrderedQuantity": 12.000,
                    "ItemCategory": "ZLLV",
                    "ProductClass": "7P",
                    "Mark": "SF-1",
                    "Material": "ROOFTOPHOOD",
                    "MaterialDescription": "ROOF TOP HOOD",
                    "PlantDescription": "WI Mfg Fac 2 Schof (AXL/INLNE)",
                    "Division": "11",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "10AA",
                    "PlantNumber": "1050",
                    "HigherLevelSalesOrderLine": "200",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV5",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0002",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0003",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0004",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0005",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0006",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0007",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0008",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0009",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0010",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0011",
                            "TagName": "SF-1"
                        },
                        {
                            "Tag": "0012",
                            "TagName": "SF-1"
                        }
                    ],
                    "Multiplier": 0.4482,
                    "TotalListPrice": 41136.00,
                    "TotalNetPrice": 18437.16,
                    "TotalBillingPrice": 18437.16,
                    "TotalDiscountPrice": 22698.84
                },
                {
                    "SalesOrderLineNumber": "30",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "BD100-12X12",
                    "ShortModelName": "null",
                    "OrderedQuantity": 1.000,
                    "ItemCategory": "ZSTK",
                    "ProductClass": "D10",
                    "Mark": "EF-1",
                    "Material": "BD100-12X12",
                    "MaterialDescription": "DMPR,BD100-12X12",
                    "PlantDescription": "WI Mfg Fac 11 Mosinee (DMPR)",
                    "Division": "60",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "60AC",
                    "PlantNumber": "1100",
                    "HigherLevelSalesOrderLine": "10",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV7",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-1"
                        }
                    ],
                    "Multiplier": 0.4562,
                    "TotalListPrice": 85.00,
                    "TotalNetPrice": 38.78,
                    "TotalBillingPrice": 38.78,
                    "TotalDiscountPrice": 46.22
                },
                {
                    "SalesOrderLineNumber": "50",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "G-095-D-8-1-17-X",
                    "ShortModelName": "null",
                    "OrderedQuantity": 3.000,
                    "ItemCategory": "ZLLV",
                    "ProductClass": "3A",
                    "Mark": "EF-2,3,4",
                    "Material": "G-095",
                    "MaterialDescription": "G-095 CENTR ROOF EXH FAN",
                    "PlantDescription": "WI Mfg Fac 2 Schof (PRV)",
                    "Division": "13",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "13CA",
                    "PlantNumber": "1110",
                    "HigherLevelSalesOrderLine": "40",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV7",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-2"
                        },
                        {
                            "Tag": "0002",
                            "TagName": "EF-3"
                        },
                        {
                            "Tag": "0003",
                            "TagName": "EF-4"
                        }
                    ],
                    "Multiplier": 0.4562,
                    "TotalListPrice": 2175.00,
                    "TotalNetPrice": 992.24,
                    "TotalBillingPrice": 992.24,
                    "TotalDiscountPrice": 1182.76
                },
                {
                    "SalesOrderLineNumber": "60",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "BD100-10X10",
                    "ShortModelName": "null",
                    "OrderedQuantity": 3.000,
                    "ItemCategory": "ZSTK",
                    "ProductClass": "D10",
                    "Mark": "EF-2,3,4",
                    "Material": "BD100-10X10",
                    "MaterialDescription": "DMPR,BD100-10X10",
                    "PlantDescription": "WI Mfg Fac 11 Mosinee (DMPR)",
                    "Division": "60",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "60AC",
                    "PlantNumber": "1100",
                    "HigherLevelSalesOrderLine": "40",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV7",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-2"
                        },
                        {
                            "Tag": "0002",
                            "TagName": "EF-3"
                        },
                        {
                            "Tag": "0003",
                            "TagName": "EF-4"
                        }
                    ],
                    "Multiplier": 0.4562,
                    "TotalListPrice": 243.00,
                    "TotalNetPrice": 110.86,
                    "TotalBillingPrice": 110.86,
                    "TotalDiscountPrice": 132.14
                },
                {
                    "SalesOrderLineNumber": "80",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "G-095-D-8-1-17-X",
                    "ShortModelName": "null",
                    "OrderedQuantity": 2.000,
                    "ItemCategory": "ZLLV",
                    "ProductClass": "3A",
                    "Mark": "EF-5,6",
                    "Material": "G-095",
                    "MaterialDescription": "G-095 CENTR ROOF EXH FAN",
                    "PlantDescription": "WI Mfg Fac 2 Schof (PRV)",
                    "Division": "13",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "13CA",
                    "PlantNumber": "1110",
                    "HigherLevelSalesOrderLine": "70",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV7",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-5"
                        },
                        {
                            "Tag": "0002",
                            "TagName": "EF-6"
                        }
                    ],
                    "Multiplier": 0.4562,
                    "TotalListPrice": 1450.00,
                    "TotalNetPrice": 661.49,
                    "TotalBillingPrice": 661.49,
                    "TotalDiscountPrice": 788.51
                },
                {
                    "SalesOrderLineNumber": "90",
                    "SalesOffice": "1030",
                    "SalesGroup": "006",
                    "Model": "BD100-10X10",
                    "ShortModelName": "null",
                    "OrderedQuantity": 2.000,
                    "ItemCategory": "ZSTK",
                    "ProductClass": "D10",
                    "Mark": "EF-5,6",
                    "Material": "BD100-10X10",
                    "MaterialDescription": "DMPR,BD100-10X10",
                    "PlantDescription": "WI Mfg Fac 11 Mosinee (DMPR)",
                    "Division": "60",
                    "CreditBlock": "null",
                    "CreditBlockDescription": "null",
                    "DeliveryBlock": "null",
                    "RequestedDeliveryDate": "2024-05-17T00:00:00",
                    "BillingInvoiceDate": "null",
                    "ProcessingStatus": "A",
                    "MaterialGroup": "60AC",
                    "PlantNumber": "1100",
                    "HigherLevelSalesOrderLine": "70",
                    "DiscountRequestNumber": "51325055",
                    "PricingCategory": "FV7",
                    "RejectCode": "null",
                    "MarkTags": [
                        {
                            "Tag": "0001",
                            "TagName": "EF-5"
                        },
                        {
                            "Tag": "0002",
                            "TagName": "EF-6"
                        }
                    ],
                    "Multiplier": 0.4562,
                    "TotalListPrice": 162.00,
                    "TotalNetPrice": 73.90,
                    "TotalBillingPrice": 73.90,
                    "TotalDiscountPrice": 88.10
                }
            ],
            "Shipments": []
        }
    ],
    "Leads": []
}


# JSON Schema object that the above JSON value conforms to
json_schema = {
	"$schema": "http://json-schema.org/draft-07/schema#",
	"description": "Schema for a sales details",
	"type": "object",
	"properties": {
		"Header": {
			"type": "object",
			"properties": {
				"SalesOrg": {"description": "", "type": "string"},
				"Trademark": {"description": "", "type": "string"},
				"SalesOrderNumber": {"description": "", "type": "string"},
				"OrderType": {"description": "", "type": "string"},
				"SalesDocumentVersionNumber": {"description": "", "type": "string"},
				"SalesOfficeNumber": {"description": "", "type": "string"},
				"OrderDate": {"description": "", "type": "string"},
				"JobName": {"description": "", "type": "string"},
				"PurchaseOrderNumber": {"description": "", "type": "string"},
				"CustomerPurchaseOrderNumber": {"description": "", "type": "string"},
				"SalesPersonId": {"description": "", "type": "string"},
				"SalesPersonName": {"description": "", "type": "string"},
				"SalesPersonEmail": {"description": "", "type": "string"},
				"Z5PartnerNumber": {"description": "", "type": "string"},
				"Incoterms": {"description": "", "type": "string"},
				"OrderTotal": {"description": "", "type": "string"},
				"Currency": {"description": "", "type": "string"},
				"PricingProcedure": {"description": "", "type": "string"},
				"InternationalOrder": {"description": "", "type": "string"},
			}
		},
		
		"Partners": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"PartnerId": {"description": "", "type": "string"},
					"PartnerType": {"description": "", "type": "string"},
					"Name": {"description": "", "type": "string"},
					"Company": {"description": "", "type": "string"},
					"AddressLine1": {"description": "", "type": "string"},
					"AddressLine2": {"description": "", "type": "string"},
					"AddressLine3": {"description": "", "type": "string"},
					"AddressLine4": {"description": "", "type": "string"},
					"Country": {"description": "", "type": "string"},
					"State": {"description": "", "type": "string"},
					"City": {"description": "", "type": "string"},
					"Zip": {"description": "", "type": "string"},
					"Fax": {"description": "", "type": "string"},
					"Phone": {"description": "", "type": "string"},
					"Email": {"description": "", "type": "string"},
				}
			}
		},
		
		"Notes": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"NoteTypeCode": {"description": "", "type": "string"},
					"NoteTypeDescription": {"description": "", "type": "string"},
					"Note": {"description": "", "type": "string"}
				}
			}
		},
		"DeliveryGroups": {
			"description": "",
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"DeliveryGroupNumber": {"description": "", "type": "string"},
					"DeliveryPriority": {"description": "", "type": "string"},
					"DeliveryPriorityDescription": {"description": "", "type": "string"},
					"MessageText": {"description": "", "type": "string"},
					"OverallStatus": {"description": "", "type": "string"},
					"OverallStatusAdditionalText": {"description": "", "type": "string"},
					"HoldStatus": {"description": "", "type": "string"},
					"PromiseDate": {"description": "", "type": "string"},
					"RepromiseDate": {"description": "", "type": "string"},
					
					"Lines": {
						"description": "",
						"type": "array",
						"items": {
							"type": "object",
							"properties": {
								"SalesOrderLineNumber ": {"description": "", "type": "string"},
								"SalesOffice ": {"description": "", "type": "string"},
								"SalesGroup ": {"description": "", "type": "string"},
								"Model ": {"description": "", "type": "string"},
								"ShortModelName ": {"description": "", "type": "string"},
								"OrderedQuantity ": {"description": "", "type": "string"},
								"ItemCategory ": {"description": "", "type": "string"},
								"ProductClass ": {"description": "", "type": "string"},
								"Mark ": {"description": "", "type": "string"},
								"Material ": {"description": "", "type": "string"},
								"MaterialDescription ": {"description": "", "type": "string"},
								"PlantDescription ": {"description": "", "type": "string"},
								"Division ": {"description": "", "type": "string"},
								"CreditBlock ": {"description": "", "type": "string"},
								"CreditBlockDescription ": {"description": "", "type": "string"},
								"DeliveryBlock ": {"description": "", "type": "string"},
								"RequestedDeliveryDate ": {"description": "", "type": "string"},
								"BillingInvoiceDate ": {"description": "", "type": "string"},
								"ProcessingStatus ": {"description": "", "type": "string"},
								"MaterialGroup ": {"description": "", "type": "string"},
								"PlantNumber ": {"description": "", "type": "string"},
								"HigherLevelSalesOrderLine ": {"description": "", "type": "string"},
								"DiscountRequestNumber ": {"description": "", "type": "string"},
								"PricingCategory ": {"description": "", "type": "string"},
								"RejectCode ": {"description": "", "type": "string"},
								"MarkTags": {
									"description": "",
									"type": "array",
									"items": {
										"type": "object",
										"properties": {
											"Tag": {"description": "", "type": "string"},
											"TagName": {"description": "", "type": "string"}
										}
									}
								},
								"Multiplier ": {"description": "", "type": "string"},
								"TotalListPrice ": {"description": "", "type": "string"},
								"TotalNetPrice ": {"description": "", "type": "string"},
								"TotalBillingPrice ": {"description": "", "type": "string"},
								"TotalDiscountPrice ": {"description": "", "type": "string"}
							}
							
						}
					},
					"Shipments": {
						"description": "",
						"type": "array",
						"items": {
							"type": "object",
							"properties": {
								"OutboundNumber": {"description": "", "type": "string"},
								"ShipmentNumber": {"description": "", "type": "string"},
								"DeliveryGroupNumber": {"description": "", "type": "string"},
								"GoodsIssueDate": {"description": "", "type": "string"},
								"CarrierCode": {"description": "", "type": "string"},
								"CarrierName": {"description": "", "type": "string"},
								"CarrierUrl": {"description": "", "type": "string"},
								"CarrierScacCode": {"description": "", "type": "string"},
								"OutboundCreationDate": {"description": "", "type": "string"},
								"ShipmentType": {"description": "", "type": "string"},
								"ShipmentTypeDescription": {"description": "", "type": "string"},
								"EquipmentTypeCode": {"description": "", "type": "string"},
								"EquipmentTypeDescription": {"description": "", "type": "string"},
								"ShippingPlant": {"description": "", "type": "string"},
								"ShippingPlantDescription": {"description": "", "type": "string"},
								"EchoShippingAccountNumber": {"description": "", "type": "string"},
								"ForwardingAgent": {"description": "", "type": "string"},
								"ForwardingAgentTrackingId": {"description": "", "type": "string"},
								"ShipmentTrackingNumber": {"description": "", "type": "string"},
								"LoadOnDate": {"description": "", "type": "string"},
								"ShipmentDescription": {"description": "", "type": "string"},
								"ExternalIdentification1": {"description": "", "type": "string"},
								"ExternalIdentification2": {"description": "", "type": "string"},
								"ShipmentText": {"description": "", "type": "string"},
								"ShipmentStatus": {"description": "", "type": "string"},
								"EstimatedDeliveryDate": {"description": "", "type": "string"},
								"DepartedDate": {"description": "", "type": "string"},
								"LoadIndicator": {"description": "", "type": "string"},
								
								"Lines": {
									"description": "",
									"type": "array",
									"items": {
										"type": "object",
										"properties": {
											"SalesOrderLineNumber": {"description": "Reference to the lines which indicate the sub-package in the delivery group", "type": "string"},
											"ShippedQuantity": {"description": "total shipped quantity for the line number", "type": "integer"}
										}
									}
								},
								"DeliveryNotes": {
									"description": "",
									"type": "array",
									"items": {
										"type": "object",
										"properties": {
											"NoteCode": {"description": "", "type": "string"},
											"NoteDesc": {"description": "", "type": "string"},
											"City": {"description": "", "type": "string"},
											"State": {"description": "", "type": "string"},
											"Timestamp": {"description": "", "type": "string"}
										}

									}
								}
							}
						}
					}
				}
			}
		}
	}
}
llm = OpenAI(model="gpt-4")

nl_query_engine = JSONQueryEngine(
    json_value=json_value,
    json_schema=json_schema,
    llm=llm,
)



#What is the value of PartnerId and PartnerType
#What is the value of MarkTags in DeliveryGroupNumber 1
# What is the value of Shipments MarkTags in DeliveryGroupNumber 1

# nl_response = nl_query_engine.query(
#     "What is the value of number of Shipments MarkTags in DeliveryGroupNumber 1",
# )
# nl_response = nl_query_engine.query(
#     "What is the value of SalesOrderNumber?",
# )
nl_response = nl_query_engine.query(
    "Do we have any shipments for delivery group number 2 and is shipment deliverd to the customer based on Delivery Notes?",
)



print("*"*25)
print(nl_response)

