import json
from mimesis.schema import Field, Schema

_ = Field('en')
schema_tender_GPA = {
    "tender": {
        "title": "tender title",
        "description": _('text.word'),
        "otherCriteria": {
            "reductionCriteria": "scoring",
            "qualificationSystemMethods": [
                "automated"
            ]
        },
        "secondStage": {
            "minimumCandidates": 2,
            "maximumCandidates": 5
        },
        "procurementMethodRationale": _('text.word'),
        "procurementMethodAdditionalInfo": "tenderprocurementMethodAdditionalInfo",
        "procurementMethodModalities": [
            "electronicAuction"
        ],
        "electronicAuctions": {
            "details": [
                {
                    "id": "1",
                    "relatedLot": "{{lot-id-1}}",
                    "electronicAuctionModalities": [
                        {
                            "eligibleMinimumDifference": {
                                "amount": 1,
                                "currency": "EUR"
                            }
                        }
                    ]
                }
            ]
        },
        "procuringEntity": {
            "id": "MD-IDNO-123654789000",
            "persones": [
                {
                    "title": "persones.title",
                    "name": "persones.name",
                    "identifier": {
                        "scheme": "MD-IDNO",
                        "id": "88888000",
                        "uri": "http://petrusenko.com/illia"
                    },
                    "businessFunctions": [
                        {
                            "id": "businessFunctions id",
                            "type": "chairman",
                            "jobTitle": "Chief Executive Officer",
                            "period": {
                                "startDate": "2019-10-30T00:00:35Z"
                            },
                            "documents": [
                                {
                                    "id": "65663734-611f-4bc7-98c9-90c6c3123598-1591028217084",
                                    "documentType": "regulatoryDocument",
                                    "title": "doc title",
                                    "description": "doc description"
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "lots": [
            {
                "id": "5632dbf4-75ad-4f78-b723-66e2339a9d52",
                "internalId": "22",
                "title": "lots title",
                "description": "lots description",
                "value": {
                    "amount": 10,
                    "currency": "EUR"
                },
                "contractPeriod": {
                    "startDate": "2020-06-29T10:30:40Z",
                    "endDate": "2020-06-30T10:30:40Z"
                },
                "placeOfPerformance": {
                    "address": {
                        "streetAddress": "placeOfPerformance streetAddress",
                        ">postalCode": "placeOfPerformance postalCode",
                        "addressDetails": {
                            "country": {
                                "id": "MD"
                            },
                            "region": {
                                "id": "1000000"
                            },
                            "locality": {
                                "scheme": "locality scheme",
                                "id": "locality id",
                                "description": "locality description"
                            }
                        }
                    },
                    "description": "description"
                }
            }
        ],
        "items": [
            {
                "id": "beb726cc-8844-4e15-87d8-68addfe29cb5",
                "internalId": "75875",
                "classification": {
                    "scheme": "CPV",
                    "description": "items description",
                    "id": "15500000-3"
                },
                "additionalClassifications": [
                    {
                        "scheme": "CPVS",
                        "description": "additionalClassifications description",
                        "id": "AB06-7"
                    }
                ],
                "quantity": 1,
                "unit": {
                    "id": "121",
                    "name": "square"
                },
                "description": "items description",
                "relatedLot": "5632dbf4-75ad-4f78-b723-66e2339a9d52"
            }
        ],
        "awardCriteria": "priceOnly",
        "awardCriteriaDetails": "automated",
        "documents": [
            {
                "documentType": "billOfQuantity",
                "id": "af8a1ede-226e-4edf-a273-d9c3ba217be2-1591026439835",
                "title": _('text.word')
            }
        ]
    }

}

print(json.dumps(schema_tender_GPA,indent=4))