from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import ExcelData, ExcelDataSomExe

# Register your models here.

# @admin.register(ExcelData)
# class ExcelDataAdmin(ImportExportModelAdmin):
#     list_display = ('UPDUSERCD1','SOKEY','DELIVERYCD','ACTFLG','PICKBATCHKEY','ASSYKEY','SOTYPE','STS','ORDERDATE','DELIVNAME',
#                     'SHIPSCHDATE','SHIPDATE','PRIORITIES','OWNERCD','ITEMCD','EXPECTQTY1','SHIPPEDQTY1','CUSTOMERCD','OWNERNM','ORDERTYPE',
#                     'DELIVSCHDATE','DELIVDATE','TRANSPORTPRIORITY','WAREHOUSECD','OTHERREFNO3','WAREHOUSENM','PREKEY','CUSTOMERNM','SHIPTOCD','SHIPTONM',
#                     'ADDRESS1','ADDRESS2','POSTNO1','POSTNO2','HPNO','EMAIL','REFNAME','ALLOCGROUP','NOTES','OTHERREFNO1',
#                     'OTHERREFNO2','MOVEKEY','WBKEY','ADDDATETIME','ADDUSERCD','UPDDATETIME','UPDUSERCD','TERMINALCD','ORDERCUSTNAME','ORDERCUSTPHONE',
#                     'ORDERCUSTHP','PHONENO','SOKEY1','SOLINENO','ORDERKEY','ORDERLINENO','ITEMGROUP','IFITEMCD','LOT1','LOT2',
#                     'LOT3','LOT4','LOT5','NOSHIPPINGFLG','OTHERFLG','XDOCKQTY1','ALLOCQTY1','PICKEDQTY1','SORTEDQTY1','ADJUSTQTY1',
#                     'PRICE1','PRICE2','PRICE3','NOTES1','LOTRESERVEFLG','PICKQTYERRORFLG','XDOCFLG','MOVELINENO','ASSYLINENO','ADDDATETIME1',
#                     'ADDUSERCD1','UPDDATETIME1','TERMINALCD1','SHOPITEMCD','OTHERVALUE1','OTHERVALUE2','FAX1','CONFIRMQTY','NAME','CONDATE',
#                     'CRUD','SODAY','IFDATE','IFSODAY'
#                  )
@admin.register(ExcelData)
class ExcelDataAdmin(ImportExportModelAdmin):
    list_display = ('dlivr_decsn_oprto_cd','dlivr_no','delvr_cd','dlivr_prgrs_stts_nm','btch_prces_no','sppm_key_no','dlivr_tpe_sctin_nm','dlivr_stts_sctin_nm','order_dtm','rcrt_phsph_nm','dlivr_prrrg_dtm',
                    'dlivr_cmple_dtm','dlivr_orer','owr_cd','prlst_cd','dlivr_prrrg_qntt','dlivr_cmple_qntt','bscnn_cd','owr_nm','order_tpe_sctin_nm','delvr_prrrg_dtm',
                    'delvr_dtm','delvr_prrt','wrhs_cd','dt_acto_stre_dlivr_no','dlivr_wrhs_nm','shpmn_dirct_no','bscnn_nm','dlgds_offce_cd','dlgds_offce_nm','dlgds_offce_bss_addr',
                    'rcrt_phsph_dtadd','post_no','postno2','pinch_mtlno','pinch_email','bscnn_rfrnc_nm','assgn_group_nm','rmrk','etc_mtter1','etc_mtter2',
                    'mvmnt_key_no','trnso_headr_no','dlivr_order_crtin_dtm','dlivr_rgter_id1','dlivr_updt_dtm','dlivr_upusr_cd','dlivr_oprto_pc_cd1','order_cstmr_nm','order_cstmr_tlno','order_cstmr_mtlno',
                    'rcrt_phsph_tlno','clssc_key_no','clssc_lne_no','order_key_no','order_lne_no','prlst_group_cd','prlst_brcd_no','lt_attrb_nm1','lt_attrb_nm2',
                    'lt_attrb_nm3','lt_attrb_nm4','lt_attrb_nm5','un_ldng_sctin_val','etc_sctin_val','crsdk_qntt','assgn_qntt','pckn_qntt','clssc_qntt','dlivr_cncll_qntt',
                    'sal_unprc_amt','sal_amt','vat','goods_rmrk','invnr_lck_cont','lt_rsrvt_sctin_cont','crsdk_sctin_val','mvmnt_lne_no','sppm_lne_no','dlivr_rgstn_dtm',
                    'dlivr_rgter_id2','dlivr_prces_dtm','dlivr_oprto_pc_cd2','spml_prlst_no','ordno1','ordno2','rcrt_phsph_fxno','decsn_qntt','prlst_nm','dlivr_decsn_dtm',
                    'dlivr_prces_stts_cd','ctdl_delay_dcnt','bscnn_dlivr_rcipt_dtm','cmptn_dlivr_prces_delay_dcnt'
                )
# @admin.register(ExcelDataSomExe)
# class ExcelDataSomExeAdmin(ImportExportModelAdmin):
#     list_display = ('PRIORITIES','SOKEY','PREKEY','OTHERVALUE1','WAYBILLNO','MESSAGE','SOTYPE','STS','ACTFLG','OWNERCD',
#                     'ORDERDATE','SHIPDATE','SHIPSCHDATE','CUSTOMERCD','ORDERTYPE','DELIVNAME','ADDRESS1','POSTNO','ADDRESS2','PHONENO',
#                     'FAX1','EMAIL','REFNAME','CUSTOMERNM','OWNERNM','ALLOCGROUP','NOTES','OTHERREFNO2','OTHERREFNO3','PICKBATCHKEY', 
#                     'MOVEKEY','ASSYKEY','NAME','ADDDATETIME','ADDUSERCD','UPDDATETIME','UPDUSERCD','ORDERCUSTNAME','ORDERCUSTPHONE','ORDERCUSTHP',
#                     'HPNO','SOKEY1','IFITEMCD','SOLINENO','PICKQTYERRORFLG','ITEMCD','LOT1','LOT2','LOT3','EXPECTQTY1',
#                     'LOT5','NOSHIPPINGFLG','SHIPPEDOTY1','ADJUSTOTY1','OTHERFLG','XDOCKQTY1','PICKEDOTY1','ALLOCQTY1','SORTEDQTY1','PRICE2',
#                     'PRICE3','NOTES1','LOTRESERVEFLG','XDOCFLG','MOVELINENO','ASSYLINENO','ADDDATETIME1','ADDUSERCD1','UPDDATETIME1','UPDUSERCD1',
#                     'TERMINALCD1','SHOPITEMCD','OTHERVALUE2','CONFIRMQTY','MANUITEMCD','CONDATE','CRUD','CATEGORY2','CATEGORY5','ITEM_GUBUN',
#                     'ITEM_BOGJONG'
#                  )
@admin.register(ExcelDataSomExe)
class ExcelDataSomExeAdmin(ImportExportModelAdmin):
    list_display = ('dlivr_orer','dlivr_no','ordno','order_prlst_no','trnso_headr_no','mssg_cont','dlivr_tpe_sctin_nm','dlivr_stts_sctin_nm','dlivr_prgrs_stts_nm','owr_cd','order_dtm',
                    'dlivr_cmple_dtm','dlivr_prrrg_dtm','bscnn_cd','order_tpe_sctin_nm','rcrt_phsph_nm','rcrt_phsph_bss_addr','post_no','rcrt_phsph_dtadd','rcrt_phsph_tlno','rcrt_phsph_fxno',
                    'rcrt_phsph_email','bscnn_rfrnc_nm','rcrt_phsph_stre_nm','owr_nm','assgn_group_nm','rmrk','sal_cos_sctin_cd','dt_acto_stre_dlivr_no','pckn_dirct_no','mvmnt_key_no',
                    'sppm_key_no','prlst_nm','dlivr_order_crtin_dtm','dlivr_rgter_id1','dlivr_updt_dtm','dlivr_upusr_cd','ordrr_nm','ordrr_tlno','ordrr_mtlno','pinch_mtlno',
                    'clssc_key_no','brcd_no','clssc_lne_no','invnr_lck_cont','prlst_cd','lt_attrb_nm1','lt_attrb_nm2','lt_attrb_nm3','dlivr_prrrg_qntt','lt_attrb_nm5',
                    'un_ldng_sctin_val','dlivr_cmple_qntt','dlivr_cncll_qntt','etc_sctin_val','crsdk_qntt','pckn_qntt','assgn_qntt','clssc_qntt','sal_amt','vat',
                    'goods_rmrk','lt_rsrvt_sctin_cont','crsdk_sctin_val','mvmnt_lne_no','sppm_lne_no','dlivr_rgstn_dtm','dlivr_rgter_id2','dlivr_prces_dtm','dlivr_decsn_oprto_cd','dlivr_oprto_pc_cd',
                    'spml_prlst_no','cstmr_pdnr_no','decsn_qntt','mkr_prduc_cd','dlivr_decsn_dtm','dlivr_prces_stts_cd','ctgry_cont','color_cd','prdct_sctin_nm','prduc_ctgry_sctin_nm'
                )