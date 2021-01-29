from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import xlrd
import pandas as pd
import sqlalchemy as db
from excelbigdata.models import Board
from django.shortcuts import redirect
from .models import ExcelData, ExcelDataSomExe
from .resources import ExcelDataResource , ExcelDataSomExeResource
from django.contrib import messages
from tablib import Dataset


# Create your views here.

def upload(request):
    #context ={}
    if  request.method == 'POST':
        upload_file = request.FILES['document']
        engine = db.create_engine('mysql://ebigdata:EncglsBig!!100@210.179.174.148:3306/enc_bigdata?charset=utf8', convert_unicode=False)
        connection = engine.raw_connection()
        metadata = db.MetaData()
        print(upload_file.name)

        if '스케쳐스출고' in upload_file.name:
            #엑셀 mysql 업로드하기
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'owr_cd':str,'post_no':str,'postno2':str,'etc_mtter2':str}
            ,usecols=[
                'dlivr_decsn_oprto_cd','dlivr_no','delvr_cd','dlivr_prgrs_stts_nm','btch_prces_no','sppm_key_no','dlivr_tpe_sctin_nm','dlivr_stts_sctin_nm','order_dtm','rcrt_phsph_nm','dlivr_prrrg_dtm',
                'dlivr_cmple_dtm','dlivr_orer','owr_cd','prlst_cd','dlivr_prrrg_qntt','dlivr_cmple_qntt','bscnn_cd','owr_nm','order_tpe_sctin_nm','delvr_prrrg_dtm',
                'delvr_dtm','delvr_prrt','wrhs_cd','dt_acto_stre_dlivr_no','dlivr_wrhs_nm','shpmn_dirct_no','bscnn_nm','dlgds_offce_cd','dlgds_offce_nm','dlgds_offce_bss_addr',
                'rcrt_phsph_dtadd','post_no','postno2','pinch_mtlno','pinch_email','bscnn_rfrnc_nm','assgn_group_nm','rmrk','etc_mtter1','etc_mtter2',
                'mvmnt_key_no','trnso_headr_no','dlivr_order_crtin_dtm','dlivr_rgter_id1','dlivr_updt_dtm','dlivr_upusr_cd','dlivr_oprto_pc_cd1','order_cstmr_nm','order_cstmr_tlno','order_cstmr_mtlno',
                'rcrt_phsph_tlno','clssc_key_no','clssc_lne_no','order_key_no','order_lne_no','prlst_group_cd','prlst_brcd_no','lt_attrb_nm1','lt_attrb_nm2',
                'lt_attrb_nm3','lt_attrb_nm4','lt_attrb_nm5','un_ldng_sctin_val','etc_sctin_val','crsdk_qntt','assgn_qntt','pckn_qntt','clssc_qntt','dlivr_cncll_qntt',
                'sal_unprc_amt','sal_amt','vat','goods_rmrk','invnr_lck_cont','lt_rsrvt_sctin_cont','crsdk_sctin_val','mvmnt_lne_no','sppm_lne_no','dlivr_rgstn_dtm',
                'dlivr_rgter_id2','dlivr_prces_dtm','dlivr_oprto_pc_cd2','spml_prlst_no','ordno1','ordno2','rcrt_phsph_fxno','decsn_qntt','prlst_nm','dlivr_decsn_dtm',
                'dlivr_prces_stts_cd','ctdl_delay_dcnt','bscnn_dlivr_rcipt_dtm','cmptn_dlivr_prces_delay_dcnt'
            ])
            table = db.Table('tb_en_skx_dlivr_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_skx_dlivr_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_skx_dlivr_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '스케쳐스입고' in upload_file.name:
            #엑셀 mysql 업로드하기
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'bscnn_cd':str, 'cmpn_cd':str, 'owr_cd':str}
            ,usecols=[
                'wrhsn_no','bscnn_cd','bscnn_nm','wrhsn_type_cd','prlst_brcd_no','wrhsn_stts_sctin_nm','wrhsn_prrrg_dtm',
                'wrhsn_cmple_dtm','wrhs_cd','lt_attrb_nm1','prrrg_wrhsn_qntt','rtwr_qntt','wrhsn_wrhs_nm','bscnn_bss_addr',
                'wrhsn_dirct_no','bscnn_dtadd','rmrk','cmpn_cd','cmpn_nm','wrhsn_prlst_no','prlst_group_cd','prcrc_dtm','prlst_cd',
                'owr_cd','prlst_nm','prlst_rmrk','wrhsn_prces_stts_cd','owr_nm','bscnn_wrhsn_rcipt_dtm','wrhsn_dirct_pinch_nm'
            ])
            table = db.Table('tb_en_skx_wrhsn_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_skx_wrhsn_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_skx_wrhsn_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '스케쳐스반품' in upload_file.name:
            #엑셀 mysql 업로드하기
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'owr_cd':str , 'cmpn_cd':str , 'companycd1':str})
            table = db.Table('tb_en_skx_rtgds_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_skx_rtgds_stats_s_02',con=engine, if_exists='append', index=False)
            print('프로시저 시작')
            cursor = connection.cursor()
            print('프로시저 중간')
            cursor.callproc("tb_en_skx_rtgds_pro")
            results = list(cursor.fetchall())
            connection.commit()
            print('프로시저 끝')
            cursor.close()
        elif '쏨니아출고' in upload_file.name:
            #엑셀 mysql 업로드하기
            # df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'BSCNN_CD':str, 'OWR_CD':str, 'POST_NO':str})
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'bscnn_cd':str, 'owr_cd':str, 'post_no':str})
            table = db.Table('tb_en_som_dlivr_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_som_dlivr_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_som_dlivr_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '쏨니아입고' in upload_file.name:
            #엑셀 mysql 업로드하기
            # df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'BSCNN_CD':str, 'CMPN_CD':str, 'OWR_CD':str})
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'bscnn_cd':str, 'cmpn_cd':str, 'owr_cd':str})
            table = db.Table('tb_en_som_wrhsn_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_som_wrhsn_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_som_wrhsn_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '쏨니아반품' in upload_file.name:
            #엑셀 mysql 업로드하기
            # df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'BSCNN_CD':str, 'CMPN_CD':str, 'OWR_CD':str})
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'bscnn_cd':str, 'cmpn_cd':str, 'owr_cdOWR_CD':str})
            table = db.Table('tb_en_som_rtgds_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_som_rtgds_stats_s_02',con=engine, if_exists='append', index=False)
            #print('프로시저 시작')
            #cursor = connection.cursor()
            #print('프로시저 중간')
            #cursor.callproc("tb_en_som_rtgds_pro")
            #results = list(cursor.fetchall())
            #connection.commit()
            #print('프로시저 끝')
            #cursor.close()
        elif '공동물류출고' in upload_file.name:
            #엑셀 mysql 업로드하기
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl')
            table = db.Table('tb_en_com_dlivr_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_com_dlivr_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_com_dlivr_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '공동물류입고' in upload_file.name:
            #엑셀 mysql 업로드하기
            # df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl'
            # ,usecols=[
            #     'OWR_CMPN_NM','IN_DIRCT_NO_1','PRCRC_NO','WRHSN_DT_1','WRHSN_TPE','WRHSN_ORER','SUPPLY_MEN_CD','ROW_NO','WRHSN_PRRRG_DT','WRHSN_DECSN_DT'
            #    ,'STTS','DTLS_STTS','ERR_MES_1','RMRK_1','RGTER_1','UPUSR_1','RGSTN_DT_1','UPDT_DT_1','UPL_ORER_1','IN_DIRCT_NO_2'              
            #    ,'GOODS_CD_1','MNFT_DT','EXPDATE','WAIT_ZNE','WRHSN_DT_2','PRRRG_QNTT','ACCPN_QNTT','CAU','GOODS_STTS','IN_LOT'
            #    ,'ACCPN_STTS','ACCPN_DECSN_DT','ADJT_STTS','RMRK_2','ERR_MES_2','RGTER_2','UPUSR_2','RGSTN_DT_2','UPDT_DT_2','UPL_ORER_2' 
            #    ,'TPE','GOODS_CD_2','GOODS_NM','USE_WHTHR','BRCD_1','BRCD_2','BRCD_3','HNDLE_CTON','UNIT_CD','UNIT_NM'    
            #    ,'SPLR','SET_GOODS_WHTHR','ACQRE_SCTIN','WRHSN_UNPRC','DLIVR_UNPRC','VAT_TPE','LRGE_CLSS','MDUM_CLSS','SML_CLSS','GOODS_BRND'          
            #    ,'GOODS_LNE','PROKND','GNDR','CTGRY','PRDCT_YR','PRDCT_SSN','PRONMBR','SIZE','COLOR','GOODS_SCTIN'     
            #    ,'STRG_TPE','STNDRD','BX_PER_QNTT','PLLT_PER_QNTT','PLLT_PER_BX_QNTT','WDTH','LNGTH','HGHT','WGHT','BX_CBM'            
            #    ,'THR_SDE_SUM','PIECE_PER_CBM','INVNR_MNGMNT','RCPTNDSBR_MNGMNT','LOT_MNGMNT','DSTRBTN_PRCSS_WHETHER','ASSGNMNT_WHETHER','EXPIRYDATE_MNGMNT_WHETHER','CNSLDTN_DSLLWNCE_WHETHER','UNIT_DLIVR' 
            #    ,'RMRK_3','RGSTN_DT_3','RGTER_3','UPDT_DT_3','UPUSR_3'
            # ])
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl'
            ,usecols=[
                'owr_cmpn_nm','in_dirct_no1','prcrc_no','wrhsn_dt1','wrhsn_tpe','wrhsn_orer','supply_men_cd','row_no','wrhsn_prrrg_dt',
                'wrhsn_decsn_dt','stts','dtls_stts','err_mes1','rmrk1','rgter1','upusr1','rgstn_dt1','updt_dt1','upl_orer1',
                'in_dirct_no2','goods_cd1','mnft_dt','expdate','wait_zne','wrhsn_dt2','prrrg_qntt','accpn_qntt','cau','goods_stts',
                'in_lot','accpn_stts','accpn_decsn_dt','adjt_stts','rmrk2','err_mes2','rgter2','upusr2','rgstn_dt2','updt_dt2',
                'upl_orer2','tpe','goods_cd2','goods_nm','use_whthr','brcd_1','brcd_2','brcd_3','hndle_cton','unit_cd','unit_nm','splr',
                'set_goods_whthr','acqre_sctin','wrhsn_unprc','dlivr_unprc','vat_tpe','lrge_clss','mdum_clss','sml_clss','goods_brnd',
                'goods_lne','proknd','gndr','ctgry','prdct_yr','prdct_ssn','pronmbr','size','color','goods_sctin','strg_tpe','stndrd',
                'bx_per_qntt','pllt_per_qntt','pllt_per_bx_qntt','wdth','lngth','hght','wght','bx_cbm','thr_sde_sum','piece_per_cbm',
                'invnr_mngmnt','rcptndsbr_mngmnt','lot_mngmnt','dstrbtn_prcss_whether','assgnmnt_whether','expirydate_mngmnt_whether',
                'cnsldtn_dsllwnce_whether','unit_dlivr','rmrk3','rgstn_dt3','rgter3','updt_dt3','upusr3'
            ])
            table = db.Table('tb_en_com_wrhsn_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_com_wrhsn_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_com_wrhsn_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '공동물류반품' in upload_file.name:
            #엑셀 mysql 업로드하기
            # df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl'
            # ,usecols=[
            #     'OWR_CMPN_NM','IN_DIRCT_NO_1','INVCE_NO','RTGDS_WRHSN_DT','RTGDS_DECSN_DT','RTGDS_TPE','RTGDS_PLC','RTGDS_MEN_NM','ORER_NO','CURR'           
            #    ,'ADDR','RTGDS_COST_SCTIN','CAU','TLNO','RMRK_1','RTGDS_STTS','RGTER_1','RGSTN_DT_1','UPUSR_1','UPDT_DT_1'              
            #    ,'ORGNL_INVCE_NO','CUST_USE_NO','IN_DIRCT_NO_2','GOODS_CD_1','RTGDS_QNTT','NRWL_QNTT','FULTY_QNTT','MNFT_DT','DSTRBTN_DT','IN_LOT'    
            #    ,'RGTER_2','RGSTN_DT_2','UPUSR_2','UPDT_DT_2','GOODS_CD_2','GOODS_NM','USE_WHTHR','BRCD_1','BRCD_2','BRCD_3'  
            #    ,'HNDLE_CTON','UNIT_CD','UNIT_NM','SPLR','SET_GOODS_WHTHR','ACQRE_SCTIN','WRHSN_UNPRC','DLIVR_UNPRC','VAT_TPE','LRGE_CLSS'        
            #    ,'MDUM_CLSS','SML_CLSS','GOODS_BRND','GOODS_LNE','PROKND','GNDR','CTGRY','PRDCT_YR','PRDCT_SSN','PRONMBR'           
            #    ,'SIZE','COLOR','GOODS_SCTIN','STRG_TPE','STNDRD','BX_PER_QNTT','PLLT_PER_QNTT','PLLT_PER_BX_QNTT','WDTH','LNGTH'             
            #    ,'HGHT','WGHT','BX_CBM','THR_SDE_SUM','PIECE_PER_CBM','INVNR_MNGMNT','RCPTNDSBR_MNGMNT','LOT_MNGMNT','DSTRBTN_PRCSS_WHETHER','ASSGNMNT_WHTHR'            
            #    ,'EXPIRYDATE_MNGMNT_WHETHER','CNSLDTN_DSLLWNCE_WHETHER','UNIT_DLIVR','RMRK','RGSTN_DT_3','RGTER_3','UPDT_DT_3','UPUSR_3'
            # ])
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl'
            ,usecols=[
                'owr_cmpn_nm','in_dirct_no1','invce_no','rtgds_wrhsn_dt','rtgds_decsn_dt','rtgds_tpe','rtgds_plc','rtgds_men_nm','orer_no','curr'
                ,'addr','rtgds_cost_sctin','cau','tlno','rmrk1','rtgds_stts','rgter1','rgstn_dt1','upusr1','updt_dt1'
                ,'orgnl_invce_no','cust_use_no','in_dirct_no2','goods_cd1','rtgds_qntt','nrwl_qntt','fulty_qntt','mnft_dt','dstrbtn_dt','in_lot'
                ,'rgter2','rgstn_dt2','upusr2','updt_dt2','goods_cd2','goods_nm','use_whthr','brcd_1','brcd_2','brcd_3'
                ,'hndle_cton','unit_cd','unit_nm','splr','set_goods_whthr','acqre_sctin','wrhsn_unprc','dlivr_unprc','vat_tpe','lrge_clss'
                ,'mdum_clss','sml_clss','goods_brnd','goods_lne','proknd','gndr','ctgry','prdct_yr','prdct_ssn','pronmbr'
                ,'size','color','goods_sctin','strg_tpe','stndrd','bx_per_qntt','pllt_per_qntt','pllt_per_bx_qntt','wdth','lngth'
                ,'hght','wght','bx_cbm','thr_sde_sum','piece_per_cbm','invnr_mngmnt','rcptndsbr_mngmnt','lot_mngmnt','dstrbtn_prcss_whether','assgnmnt_whthr'
                ,'expirydate_mngmnt_whether','cnsldtn_dsllwnce_whether','unit_dlivr','rmrk','rgstn_dt3','rgter3','updt_dt3','upusr3'
            ])
            table = db.Table('tb_en_com_rtgds_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_com_rtgds_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_com_rtgds_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '마이창고출고' in upload_file.name:
            #엑셀 mysql 업로드하기
            # df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'BRCD':str}
            # ,usecols=['DLIVR_DT','CSTMR_NM','GOODS_NM','MDL_NM','BRCD','QNTT'])
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'brcd':str}
            ,usecols=['dlivr_dt','cstmr_nm','goods_nm','mdl_nm','brcd','qntt'])
            table = db.Table('tb_en_myw_dlivr_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_myw_dlivr_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_myw_dlivr_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '마이창고입고' in upload_file.name:
            #엑셀 mysql 업로드하기
            # df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'BRCD':str}
            # ,usecols=['WRHSN_DT','CSTMR_NM','GOODS_NM','MDL_NM','BRCD','WRHSN_QNTT','RMRK'])
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl',converters={'brcd':str}
            ,usecols=['wrhsn_dt','cstmr_nm','goods_nm','mdl_nm','brcd','wrhsn_qntt','rmrk'])
            table = db.Table('tb_en_myw_wrhsn_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_myw_wrhsn_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_myw_wrhsn_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '마이창고반품' in upload_file.name:
            #엑셀 mysql 업로드하기
            # df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl'
            # ,usecols=['PRGRS_STTN','SCTIN','RQST_DT','PCIPT_DT','RCLL_DT','CSTMR_NM','ARRVL_PLC','SNR','PRXSTNC_INVCE','RTGDS_INVCE','GOODS_NM'])
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl'
            ,usecols=['prgrs_sttn','sctin','rqst_dt','pcipt_dt','rcll_dt','cstmr_nm','arrvl_plc','snr','prxstnc_invce','rtgds_invce','goods_nm'])
            table = db.Table('tb_en_myw_rtgds_stats_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_myw_rtgds_stats_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_myw_rtgds_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
        elif '월별도급인력사용량' in upload_file.name:
            #엑셀 mysql 업로드하기
            # df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl'
            # ,usecols=['PRGRS_STTN','SCTIN','RQST_DT','PCIPT_DT','RCLL_DT','CSTMR_NM','ARRVL_PLC','SNR','PRXSTNC_INVCE','RTGDS_INVCE','GOODS_NM'])
            df = pd.read_excel(io='C:/Users/Public/Documents/'+upload_file.name,sheet_name='Sheet1', engine='openpyxl'
            ,usecols=['lgst_cntr_nm', 'otsrc_cmpn_nm', 'sxdst_cd', 'otsrc_dtm', 'otsrc_nofpr_cnt'])
            table = db.Table('tb_en_mnb_otsrc_hmfrc_s_02', metadata, autoload=True, autoload_with=engine)
            df.to_sql('tb_en_mnb_otsrc_hmfrc_s_02',con=engine, if_exists='append', index=False)
            # print('프로시저 시작')
            # cursor = connection.cursor()
            # print('프로시저 중간')
            # cursor.callproc("tb_en_mnb_otsrc_hmfrc_pro")
            # results = list(cursor.fetchall())
            # connection.commit()
            # print('프로시저 끝')
            # cursor.close()
          
        return redirect('/admin/excelbigdata/exceldata/')

    return render(request,'upload.html')


def home(request):
    return render(request, "home.html")

def board(request):
    rsBoard = Board.objects.all()

    return render(request, "board_list.html",
    {
        'rsBoard': rsBoard
    })

def board_write(request):
    return render(request, "board_write.html",)

def board_insert(request): 
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if btitle != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote,b_writer=bwriter)
        return redirect('/board')
    
    else:
        return redirect('/board_write')


#엑셀 Mysql
def simple_upload(request):
    if request.method == 'POST':
        excelData_resource = ExcelDataResource()
        dataset = Dataset()
        new_person = request.FILES['document']

        if not new_person.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')

        imported_data = dataset.load(new_person.read(),format='xlsx')
   
        for data in imported_data:
            value = ExcelData(
                data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],
                data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],
                data[21],data[22],data[23],data[24],data[25],data[26],data[27],data[28],data[29],data[30],
                data[31],data[32],data[33],data[34],data[35],data[36],data[37],data[38],data[39],data[40],
                data[41],data[42],data[43],data[44],data[45],data[46],data[47],data[48],data[49],data[50],
                data[51],data[52],data[53],data[54],data[55],data[56],data[57],data[58],data[59],data[60],
                data[61],data[62],data[63],data[64],data[65],data[66],data[67],data[68],data[69],data[70],
                data[71],data[72],data[73],data[74],data[75],data[76],data[77],data[78],data[79],data[80],
                data[81],data[82],data[83],data[84],data[85],data[86],data[87],data[88],data[89],data[90],
                data[91],data[91],data[93]
            )
            value.save()
    return render(request,'upload.html')


#엑셀 Mysql 쏨니아 출고
def excelDataSomExe(request):
    if request.method == 'POST':
        excelData_resource = ExcelDataSomExeResource()
        dataset = Dataset()
        new_person = request.FILES['document']

        if not new_person.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')

        imported_data = dataset.load(new_person.read(),format='xlsx')
   
        for data in imported_data:
            value = ExcelData(
                data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],
                data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20],
                data[21],data[22],data[23],data[24],data[25],data[26],data[27],data[28],data[29],data[30],
                data[31],data[32],data[33],data[34],data[35],data[36],data[37],data[38],data[39],data[40],
                data[41],data[42],data[43],data[44],data[45],data[46],data[47],data[48],data[49],data[50],
                data[51],data[52],data[53],data[54],data[55],data[56],data[57],data[58],data[59],data[60],
                data[61],data[62],data[63],data[64],data[65],data[66],data[67],data[68],data[69],data[70],
                data[71],data[72],data[73],data[74],data[75],data[76],data[77],data[78],data[79],data[80]
            )
            value.save()
    return render(request,'upload.html')
