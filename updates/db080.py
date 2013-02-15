#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Переводим все таблицы в БД из MyISAM в InnoDB
'''


def upgrade(conn):
    global config    
    c = conn.cursor()

    tables = [
            "Account                              ",
            "Account_Item                         ",
            "Action                               ",
            "ActionProperty                       ",
            "ActionPropertyTemplate               ",
            "ActionPropertyType                   ",
            "ActionProperty_Action                ",
            "ActionProperty_CureEpicrisis         ",
            "ActionProperty_Date                  ",
            "ActionProperty_DiagnosticEpicrisis   ",
            "ActionProperty_Double                ",
            "ActionProperty_FDRecord              ",
            "ActionProperty_HospitalBed           ",
            "ActionProperty_Image                 ",
            "ActionProperty_ImageMap              ",
            "ActionProperty_Integer               ",
            "ActionProperty_Job_Ticket            ",
            "ActionProperty_MKB                   ",
            "ActionProperty_OrgStructure          ",
            "ActionProperty_Organisation          ",
            "ActionProperty_Person                ",
            "ActionProperty_String                ",
            "ActionProperty_Time                  ",
            "ActionProperty_rbFinance             ",
            "ActionProperty_rbReasonOfAbsence     ",
            "ActionTemplate                       ",
            "ActionTissue                         ",
            "ActionType                           ",
            "ActionType_EventType_check           ",
            "ActionType_QuotaType                 ",
            "ActionType_Service                   ",
            "ActionType_TissueType                ",
            "Address                              ",
            "AddressAreaItem                      ",
            "AddressHouse                         ",
            "AppLock                              ",
            "AppLock_Detail                       ",
            "AssignmentHour                       ",
            "Bank                                 ",
            "BlankActions                         ",
            "BlankActions_Moving                  ",
            "BlankActions_Party                   ",
            "BlankTempInvalid_Moving              ",
            "BlankTempInvalid_Party               ",
            "BlankTempInvalids                    ",
            "CalendarExceptions                   ",
            "Client                               ",
            "ClientAddress                        ",
            "ClientAllergy                        ",
            "ClientAttach                         ",
            "ClientContact                        ",
            "ClientDocument                       ",
            "ClientFDProperty                     ",
            "ClientFlatDirectory                  ",
            "ClientIdentification                 ",
            "ClientIntoleranceMedicament          ",
            "ClientPolicy                         ",
            "ClientRelation                       ",
            "ClientSocStatus                      ",
            "ClientWork                           ",
            "ClientWork_Hurt                      ",
            "ClientWork_Hurt_Factor               ",
            "Client_Quoting                       ",
            "Client_QuotingDiscussion             ",
            "Contract                             ",
            "Contract_Contingent                  ",
            "Contract_Contragent                  ",
            "Contract_Specification               ",
            "Contract_Tariff                      ",
            "CouponsTransferQuotes                ",
            "Diagnosis                            ",
            "Diagnostic                           ",
            "EmergencyBrigade                     ",
            "EmergencyBrigade_Personnel           ",
            "EmergencyCall                        ",
            "Event                                ",
            "EventType                            ",
            "EventTypeForm                        ",
            "EventType_Action                     ",
            "EventType_Diagnostic                 ",
            "Event_Feed                           ",
            "Event_LocalContract                  ",
            "Event_Payment                        ",
            "Event_Persons                        ",
            "FDField                              ",
            "FDFieldType                          ",
            "FDFieldValue                         ",
            "FDRecord                             ",
            "FlatDirectory                        ",
            "InformerMessage                      ",
            "InformerMessage_readMark             ",
            "Job                                  ",
            "Job_Ticket                           ",
            "LastChanges                          ",
            "Licence                              ",
            "Licence_Service                      ",
            "MKB                                  ",
            "MKB_QuotaType_PacientModel           ",
            #"Meta                                 ",
            "ModelDescription                     ",
            "NotificationOccurred                 ",
            "OrgStructure                         ",
            "OrgStructure_ActionType              ",
            "OrgStructure_Address                 ",
            "OrgStructure_DisabledAttendance      ",
            "OrgStructure_EventType               ",
            "OrgStructure_Gap                     ",
            "OrgStructure_HospitalBed             ",
            "OrgStructure_Job                     ",
            "OrgStructure_Stock                   ",
            "Organisation                         ",
            "Organisation_Account                 ",
            "Organisation_PolicySerial            ",
            "Person                               ",
            "PersonAddress                        ",
            "PersonDocument                       ",
            "PersonEducation                      ",
            "PersonOrder                          ",
            "PersonTimeTemplate                   ",
            "Person_Activity                      ",
            "Person_Profiles                      ",
            "Person_TimeTemplate                  ",
            "QuotaType                            ",
            "Quoting                              ",
            "QuotingBySpeciality                  ",
            "QuotingByTime                        ",
            "Quoting_Region                       ",
            "Setting                              ",
            "SocStatus                            ",
            "StockMotion                          ",
            "StockMotion_Item                     ",
            "StockRecipe                          ",
            "StockRecipe_Item                     ",
            "StockRequisition                     ",
            "StockRequisition_Item                ",
            "StockTrans                           ",
            "TakenTissueJournal                   ",
            "TempInvalid                          ",
            "TempInvalidDuplicate                 ",
            "TempInvalid_Period                   ",
            "Tissue                               ",
            "VariablesforSQL                      ",
            "Versions                             ",
            "Visit                                ",
            "action_document                      ",
            "mrbModelAgeGroup                     ",
            "mrbModelAidCase                      ",
            "mrbModelAidPurpose                   ",
            "mrbModelCategory                     ",
            "mrbModelContinuation                 ",
            "mrbModelDiseaseClass                 ",
            "mrbModelExpectedResult               ",
            "mrbModelInstitutionType              ",
            "mrbModelSertificationRequirement     ",
            "mrbModelStateBadness                 ",
            "rb64District                         ",
            "rb64PlaceType                        ",
            "rb64Reason                           ",
            "rb64StreetType                       ",
            "rbAcademicDegree                     ",
            "rbAcademicTitle                      ",
            "rbAccountExportFormat                ",
            "rbAccountingSystem                   ",
            "rbActionShedule                      ",
            "rbActionShedule_Item                 ",
            "rbActivity                           ",
            "rbAgreementType                      ",
            "rbAnalysisStatus                     ",
            "rbAttachType                         ",
            "rbBlankActions                       ",
            "rbBlankTempInvalids                  ",
            "rbBloodType                          ",
            "rbCashOperation                      ",
            "rbComplain                           ",
            "rbContactType                        ",
            "rbCoreActionProperty                 ",
            "rbCounter                            ",
            "rbDiagnosisType                      ",
            "rbDiet                               ",
            "rbDiseaseCharacter                   ",
            "rbDiseasePhases                      ",
            "rbDiseaseStage                       ",
            "rbDispanser                          ",
            "rbDocumentType                       ",
            "rbDocumentTypeGroup                  ",
            "rbEmergencyAccident                  ",
            "rbEmergencyCauseCall                 ",
            "rbEmergencyDeath                     ",
            "rbEmergencyDiseased                  ",
            "rbEmergencyEbriety                   ",
            "rbEmergencyMethodTransportation      ",
            "rbEmergencyPlaceCall                 ",
            "rbEmergencyPlaceReceptionCall        ",
            "rbEmergencyReasondDelays             ",
            "rbEmergencyReceivedCall              ",
            "rbEmergencyResult                    ",
            "rbEmergencyTransferredTransportation ",
            "rbEmergencyTypeAsset                 ",
            "rbEventProfile                       ",
            "rbEventTypePurpose                   ",
            "rbFinance                            ",
            "rbHealthGroup                        ",
            "rbHospitalBedProfile                 ",
            "rbHospitalBedShedule                 ",
            "rbHospitalBedType                    ",
            "rbHurtFactorType                     ",
            "rbHurtType                           ",
            "rbImageMap                           ",
            "rbJobType                            ",
            "rbLaboratory                         ",
            "rbLaboratory_Test                    ",
            "rbMKBSubclass                        ",
            "rbMKBSubclass_Item                   ",
            "rbMealTime                           ",
            "rbMedicalAidProfile                  ",
            "rbMedicalAidType                     ",
            "rbMedicalAidUnit                     ",
            "rbMenu                               ",
            "rbMenu_Content                       ",
            "rbMesSpecification                   ",
            "rbNet                                ",
            "rbNomenclature                       ",
            "rbOKFS                               ",
            "rbOKPF                               ",
            "rbOKVED                              ",
            "rbOperationType                      ",
            "rbPacientModel                       ",
            "rbPayRefuseType                      ",
            "rbPolicyType                         ",
            "rbPost                               ",
            "rbPrintTemplate                      ",
            "rbQuotaStatus                        ",
            "rbReasonOfAbsence                    ",
            "rbRelationType                       ",
            "rbRequestType                        ",
            "rbResult                             ",
            "rbScene                              ",
            "rbService                            ",
            "rbServiceClass                       ",
            "rbServiceGroup                       ",
            "rbServiceSection                     ",
            "rbServiceType                        ",
            "rbService_Profile                    ",
            "rbSocStatusClass                     ",
            "rbSocStatusClassTypeAssoc            ",
            "rbSocStatusType                      ",
            "rbSpecialVariablesPreferences        ",
            "rbSpeciality                         ",
            "rbTariffCategory                     ",
            "rbTempInvalidBreak                   ",
            "rbTempInvalidDocument                ",
            "rbTempInvalidDuplicateReason         ",
            "rbTempInvalidReason                  ",
            "rbTempInvalidRegime                  ",
            "rbTempInvalidResult                  ",
            "rbTest                               ",
            "rbTestTubeType                       ",
            "rbThesaurus                          ",
            "rbTimeQuotingType                    ",
            "rbTissueType                         ",
            "rbTransferDateType                   ",
            "rbTraumaType                         ",
            "rbTreatment                          ",
            "rbUnit                               ",
            "rbUserProfile                        ",
            "rbUserProfile_Right                  ",
            "rbUserRight                          ",
            "rbVisitType                          ",
            "rdFirstName                          ",
            "vclient_quoting                      ",
            "vclient_quoting_history              ",
            "vclient_quoting_sub                  ",
            "vhospitalbed                         ",
            "vjobticket                           ",
            "vrbbackwardclientrelation            ",
            "vrbdirectclientrelation              ",
            "vrbmkbz                              ",
            "vrbperson                            ",
            "vrbpersonwithspeciality              ",
            "vrbsocstatustype                     ",]
    
    for table in tables:
        tbl = table.rstrip()
        print("Change Engine for table", tbl)
        sql = u'''
        ALTER TABLE %s ENGINE=InnoDB;''' % tbl
        try:
            c.execute(sql)
        except:
            print("Table", tbl, "already use InnoDB Engine or not exists.")
    
def downgrade(conn):
    pass
