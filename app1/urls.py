from django.urls import re_path,path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^go$', views.go, name='go'),
    re_path(r'^Signup_emailval/$', views.Signup_emailval, name='Signup_emailval'),
    re_path(r'^user_name_check/$', views.user_name_check, name='user_name_check'),
    re_path(r'^godash$', views.godash, name='godash'),
    re_path(r'^logout$', views.logout, name='logout'),
    re_path(r'^something$', views.something, name='something'),
    re_path(r'^userprofile/(?P<id>\d+)$', views.userprofile, name='userprofile'),
    re_path(r'^edituserprofile$', views.edituserprofile, name='edituserprofile'),
    re_path(r'^updateuserprofile$', views.updateuserprofile, name='updateuserprofile'),
    re_path(r'^goonlinebank$', views.goonlinebank, name='goonlinebank'),
    re_path(r'^goofflinebank$', views.goofflinebank, name='goofflinebank'),
    re_path(r'^gobankrecon$', views.gobankrecon, name='gobankrecon'),
    re_path(r'^gosalesrecords$', views.gosalesrecords, name='gosalesrecords'),
    
    # re_path(r'^gocustomers$', views.customers, name='gocustomers'),

    re_path(r'^gopands$', views.gopands, name='gopands'),
    re_path(r'^goexpences$', views.goexpences, name='goexpences'),
    re_path(r'^gosupplies$', views.gosupplies, name='gosupplies'),
    re_path(r'^goaddsuppliers$', views.goaddsuppliers, name='goaddsuppliers'),
    re_path(r'^customers$', views.customers, name='customers'),
    re_path(r'^editcustomer/(?P<id>\d+)$', views.editcustomer, name='editcustomer'),
    re_path(r'^editcustomer/updatecustomer/(?P<id>\d+)$', views.updatecustomer, name='updatecustomer'),
    re_path(r'^deletecustomer/(?P<id>\d+)$', views.deletecustomer, name='deletecustomer'),

    re_path(r'^gostandard$', views.gostandard, name='gostandard'),
    re_path(r'^gocustomreports$', views.goreports, name='gocustomreports'),
    re_path(r'^gomanagementreports$', views.gomanagementreports, name='gomanagementreport'),
    re_path(r'^gotax$', views.gotax, name='gotax'),
    re_path(r'^returntaxes', views.returntaxes, name='returntaxes'),
    re_path(r'^paymenthistory', views.paymenthistory, name='paymenthistory'),
    re_path(r'^addtax', views.addtax, name='addtax'),
    re_path(r'^grouptaxes', views.grouptaxes, name='grouptaxes'),
    re_path(r'^customtaxes', views.customtaxes, name='customtaxes'),
    re_path(r'^taxrate', views.taxrate, name='taxrate'),
    re_path(r'^edittaxes', views.edittaxes, name='edittaxes'),
    re_path(r'^editsettings', views.editsettings, name='editsettings'),
    re_path(r'^taxadd1', views.taxadd1, name='taxadd1'),

    # my section

    re_path(r'^gocoa$', views.gocoa, name='gocoa'),
    re_path(r'^gocoa/coaedit/(?P<accountsid>\d+)$', views.coaedit, name='coaedit'),
    re_path(r'^gocoa/coaedit/accupdate/(?P<accountsid>\d+)$', views.accupdate, name='accupdate'),
    re_path(r'^gocoa/deleteaccount/(?P<accountsid>\d+)$', views.deleteaccount, name='deleteaccount'),
    re_path(r'^gocoa/coa1edit/(?P<accounts1id>\d+)$', views.coa1edit, name='coa1edit'),
    re_path(r'^gocoa/coa1edit/acc1update/(?P<accounts1id>\d+)$', views.acc1update, name='acc1update'),

    re_path(r'^createaccount$', views.createaccount, name='createaccount'),
    re_path(r'^gorecon$', views.gorecon, name='gorecon'),
    re_path(r'^reconcreate$', views.reconcreate, name='reconcreate'),
    re_path(r'^goreconciled$', views.goreconciled, name='goreconciled'),
    re_path(r'^editrecon/(?P<expenseid>\d+)$', views.editrecon, name='editrecon'),
    re_path(r'^editrecon1/(?P<expenseid>\d+)$', views.editrecon1, name='editrecon1'),
    re_path(r'^gomyacc$', views.gomyacc, name='gomyacc'),

    
    re_path(r'^goprintinvoice$', views.goprintinvoice, name='goprintinvoice'),
    re_path(r'^goselectpands$', views.goselectpands, name='goselectpands'),
    re_path(r'^goinv$', views.goinv, name='goinv'),
    re_path(r'^gononinv$', views.gononinv, name='gononinv'),
    re_path(r'^goser$', views.goser, name='goser'),
    re_path(r'^gobun$', views.gobun, name='gobun'),
    re_path(r'^goselpan$', views.goselpan, name='goselpan'),
    re_path(r'^goaddcust$', views.goaddcust, name='goaddcust'),

    re_path(r'^create$', views.create, name='create'),
    re_path(r'^company$', views.company, name='company'),
    re_path(r'^register/(?P<id>\d+)$$', views.register, name='register'),
    re_path(r'^regcomp$', views.regcomp, name='regcomp'),  # company register
    re_path(r'^login$', views.login, name='login'),
    re_path(r'^cust$', views.cust, name='cust'),

    re_path(r'^suppliers$', views.suppliercreate, name='suppliers'),
    re_path(r'^supedit/(?P<id>\d+)$', views.supedit, name='supedit'),
    re_path(r'^supedit/updatesup/(?P<id>\d+)$', views.updatesup, name='updatesup'),
    re_path(r'^deletesup/(?P<id>\d+)$', views.deletesup, name='deletesup'),

    re_path(r'^gopayslip$', views.gopayslip, name='gopayslip'),
    re_path(r'^addtimeactivity$', views.addtimeactivity, name='addtimeactivity'),
    re_path(r'^addbill$', views.addbill, name='addbill'),
    re_path(r'^addexpense$', views.addexpense, name='addexpense'),
    re_path(r'^addcheque$', views.addcheque, name='addcheque'),
    re_path(r'^addsuppliercredit$', views.addsuppliercredit, name='addsuppliercredit'),
    re_path(r'^addadvancepayment$', views.addadvancepayment, name='addadvancepayment'),
    re_path(r'^addpdcc$', views.addpdcc, name='addpdcc'),
    re_path(r'^pdccdelete/(?P<id>\d+)$', views.pdccdelete, name='pdccdelete'),
    re_path(r'^pdccedit/(?P<id>\d+)$', views.pdccedit, name='pdccedit'),
    re_path(r'^pdccedit/updatepdcc/(?P<id>\d+)$', views.updatepdcc, name='updatepdcc'),

    re_path(r'^advpay$', views.advpay, name='advpay'),
    re_path(r'^advpayedit/(?P<id>\d+)$', views.advpayedit, name='advpayedit'),
    re_path(r'^advpayedit/updateadvpay/(?P<id>\d+)$', views.updateadvpay, name='updateadvpay'),
    re_path(r'^deleteadvpay/(?P<id>\d+)$', views.deleteadvpay, name='deleteadvpay'),
    re_path(r'^pdcc$', views.pdcc, name='pdcc'),

    # Drishya

    re_path(r'^salesrecipts$', views.salesrecipts, name='salesrecipts'),
    re_path(r'^addsalesrecipts$', views.addsalesrecipts, name='addsalesrecipts'),
    re_path(r'^editsale/(?P<id>\d+)$', views.editsale, name='editsale'),
    re_path(r'^showsales/(?P<id>\d+)$', views.showsales, name='showsales'),
    re_path(r'^editsale/updatesale/(?P<id>\d+)$', views.updatesale, name='updatesale'),
    re_path(r'^deletesale/(?P<id>\d+)$', views.deletesale, name='deletesale'),

    re_path(r'^gotimeactivity$', views.gotimeactivity, name='gotimeactivity'),
    re_path(r'^timectivity$', views.timectivity, name='timectivity'),
    re_path(r'^edittime/(?P<id>\d+)$', views.edittime, name='edittime'),
    re_path(r'^edittime/updattime/(?P<id>\d+)$', views.updattime, name='updattime'),
    re_path(r'^deletetime/(?P<id>\d+)$', views.deletetime, name='deletetime'),

    re_path(r'^gosaletimeactivity$', views.gosaletimeactivity, name='gosaletimeactivity'),
    re_path(r'^saletimectivity$', views.saletimectivity, name='saletimectivity'),
    re_path(r'^edittimesale/(?P<id>\d+)$', views.edittimesale, name='edittimesale'),
    re_path(r'^edittimesale/updattimesale/(?P<id>\d+)$', views.updattimesale, name='updattimesale'),
    re_path(r'^deletetimesale/(?P<id>\d+)$', views.deletetimesale, name='deletetimesale'),

    re_path(r'^gocheque$', views.gocheque, name='gocheque'),
    re_path(r'^cheque$', views.cheque, name='cheque'),
    re_path(r'^editcheque/(?P<id>\d+)$', views.editcheque, name='editcheque'),
    re_path(r'^editcheque/updatecheque/(?P<id>\d+)$', views.updatecheque, name='updatecheque'),
    re_path(r'^deletecheque/(?P<id>\d+)$', views.deletecheque, name='deletecheque'),

    # sayoojya

    re_path(r'^invindex$', views.invindex, name='invindex'),
    re_path(r'^invcreate$', views.invcreate, name='invcreate'),
    re_path(r'^viewinvoice/(?P<id>\d+)$', views.viewinvoice, name='viewinvoice'),
    
    
    

    re_path(r'^gobills$', views.gobills, name='gobills'),
    re_path(r'^billcreate$', views.billcreate, name='billcreate'),
    re_path(r'^editbills/(?P<id>\d+)$', views.editbills, name='editbills'),
    re_path(r'^editbills/updatebills/(?P<id>\d+)$', views.updatebills, name='updatebills'),
    re_path(r'^deletebills/(?P<id>\d+)$', views.deletebills, name='deletebills'),

    re_path(r'^gopay$', views.gopay, name='gopay'),
    re_path(r'^goacc$', views.goacc, name='goacc'),
    re_path(r'^myac$', views.myac, name='myac'),
    re_path(r'^editmyac/(?P<id>\d+)$', views.editmyac, name='editmyac'),
    re_path(r'^editmyac/updatemyac/(?P<id>\d+)$', views.updatemyac, name='updatemyac'),
    re_path(r'^deletemyac/(?P<id>\d+)$', views.deletemyac, name='deletemyac'),

    re_path(r'^gosupcredit$', views.gosupcredit, name='gosupcredit'),
    re_path(r'^suplcreditcreate$', views.suplcreditcreate, name='suplcreditcreate'),
    re_path(r'^editsuplcredit/(?P<id>\d+)$', views.editsuplcredit, name='editsuplcredit'),
    re_path(r'^editsuplcredit/updatesuplcredit/(?P<id>\d+)$', views.updatesuplcredit, name='updatesuplcredit'),
    re_path(r'^deletesuplcredit/(?P<id>\d+)$', views.deletesuplcredit, name='deletesuplcredit'),

    # anjali

    re_path(r'^creditindex$', views.creditindex, name='creditindex'),
    re_path(r'^creditcreate$', views.creditcreate, name='creditcreate'),

    re_path(r'^paymentindex$', views.paymentindex, name='paymentindex'),
    re_path(r'^paymentcreate$', views.paymentcreate, name='paymentcreate'),
    re_path(r'^deletepayment/(?P<id>\d+)$', views.deletepayment, name='deletepayment'),
    re_path(r'^deletecredit/(?P<id>\d+)$', views.deletecredit, name='deletecredit'),
    re_path(r'^editcredit/(?P<id>\d+)$', views.editcredit, name='editcredit'),
    re_path(r'^showcredit/(?P<id>\d+)$', views.showcredit, name='showcredit'),
    re_path(r'^editcredit/updatecredit/(?P<id>\d+)$', views.updatecredit, name='updatecredit'),
    # re_path(r'^editpayment/(?P<id>\d+)$', views.editpayment, name='editpayment'),
    # re_path(r'^editpayment/updatepayment/(?P<id>\d+)$', views.updatepayment, name='updatepayment'),
    re_path(r'^expencesindex$', views.expencesindex, name='expencesindex'),
    re_path(r'^expencescreate$', views.expencescreate, name='expencescreate'),
    re_path(r'^deleteexpences/(?P<id>\d+)$', views.deleteexpences, name='deleteexpences'),
    re_path(r'^editexpences/(?P<id>\d+)$', views.editexpences, name='editexpences'),
    re_path(r'^editexpences/updateexpences/(?P<id>\d+)$', views.updateexpences, name='updateexpences'),

    # anusha

    re_path(r'^estindex$', views.estindex, name='estindex'),
    re_path(r'^estcreate$', views.estcreate, name='estcreate'),
    re_path(r'^delayed$', views.delayed, name='delayed'),
    re_path(r'^delcreate$', views.delcreate, name='delcreate'),
    re_path(r'^editestimate/(?P<id>\d+)$', views.editestimate, name='editestimate'),
    # re_path(r'^editestimate/updateestimate/(?P<id>\d+)$', views.updateestimate, name='updateestimate'),
    re_path(r'^deleteestimate/(?P<id>\d+)$', views.deleteestimate, name='deleteestimate'),
    re_path(r'^editdelayed/(?P<id>\d+)$', views.editdelayed, name='editdelayed'),
    re_path(r'^editdelayed/delayedupdate/(?P<id>\d+)$', views.delayedupdate, name='delayedupdate'),
    re_path(r'^deletedelay/(?P<id>\d+)$', views.deletedelay, name='deletedelay'),

    # drishya

    re_path(r'^addpandse$', views.addpandse, name='addpandse'),
    re_path(r'^image_upload$', views.addpandse, name='image_upload'),
    re_path(r'^editser/(?P<id>\d+)$', views.editser, name='editser'),
    re_path(r'^editser/updateser/(?P<id>\d+)$', views.updateser, name='updateser'),
    re_path(r'^deleteser/(?P<id>\d+)$', views.deleteser, name='deleteser'),

    # Anjali

    re_path(r'^addnoninv$', views.addnoninv, name='addnoninv'),
    re_path(r'^image_upload$', views.addnoninv, name='image_upload'),
    re_path(r'^addnoninv$', views.nonivndisplay, name='addnoninv'),
    re_path(r'^deletenoninv/(?P<id>\d+)$', views.deletenoninv, name='deletenoninv'),
    re_path(r'^editnoninv/(?P<id>\d+)$', views.editnoninv, name='editnoninv'),
    re_path(r'^editnoninv/noninvupdate/(?P<id>\d+)$', views.noninvupdate, name='noninvupdate'),
    re_path(r'^gogst$', views.gogst, name='gogst'),
    re_path(r'^govat$', views.govat, name='govat'),
    re_path(r'^goservicetax$', views.goservicetax, name='goservicetax'),
    re_path(r'^addtax$', views.addtax, name='addtax'),
    re_path(r'^gotaxpaymentgst$', views.gotaxpaymentgst, name='gotaxpaymentgst'),
    re_path(r'^bankrecon1$', views.bankrecon1, name='bankrecon1'),
    re_path(r'^gobankrecon2$', views.gobankrecon2, name='gobankrecon2'),

    # sayooo

    re_path(r'^addbun$', views.addbun, name='addbun'),
    re_path(r'^image_upload$', views.addbun, name='image_upload'),
    re_path(r'^bundle$', views.display, name='bundle'),
    re_path(r'^editbun/(?P<id>\d+)$', views.editbun, name='bundle'),
    re_path(r'^editbun/updatebun/(?P<id>\d+)$', views.updatebun, name='updatebun'),

    re_path(r'^editbun/updatebun/(?P<id>\d+)$', views.updatebun, name='updatebun'),
    re_path(r'^deletebun/(?P<id>\d+)$', views.deletebun, name='deletebun'),

    re_path(r'^viewpayslip/payslipcreate$', views.payslipcreate, name='payslipcreate'),

    re_path(r'^viewpayslip/(?P<employeeid>\d+)$', views.viewpayslip, name='viewpayslip'),
    re_path(r'^viewpay/(?P<payslipid>\d+)$', views.viewpay, name='viewpay'),
    re_path(r'^deletepay/(?P<payslipid>\d+)$', views.deletepay, name='deletepay'),

    re_path(r'^goemoliyee$', views.goemployee, name='goemployee'),
    re_path(r'^goaddemp$', views.goaddemp, name='goaddemp'),
    re_path(r'^Employee_gmailval/$', views.Employee_gmailval, name='Employee_gmailval'),

    re_path(r'^employees$', views.employees, name='employees'),
    re_path(r'^empedit/(?P<employeeid>\d+)$', views.empedit, name='empedit'),
    re_path(r'^empedit/updateemp/(?P<employeeid>\d+)$', views.updateemp, name='updateemp'),
    re_path(r'^deleteemp/(?P<employeeid>\d+)$', views.deleteemp, name='deleteemp'),

    re_path(r'^payedit/(?P<payslipid>\d+)$', views.payedit, name='payedit'),
    re_path(r'^payedit/updatepay/(?P<payslipid>\d+)$', views.updatepay, name='updatepay'),

    # anusha

    re_path(r'^addinv$', views.addinv, name='addinv'),
    re_path(r'^image_upload$', views.addinv, name='image_upload'),
    re_path(r'^addninv$', views.ivndisplay, name='addinv'),
    re_path(r'^deleteinv/(?P<id>\d+)', views.deleteinv, name='deleteinv'),
    re_path(r'^editinv/(?P<id>\d+)$', views.editinv, name='editinv'),
    re_path(r'^editinv/invupdate/(?P<id>\d+)$', views.invupdate, name='invupdate'),

    re_path(r'^goaddcustinvoice$', views.goaddcustinvoice, name='goaddcustinvoice'),
    re_path(r'^customersinvoice$', views.customersinvoice, name='customersinvoice'),
    re_path(r'^goaddcustpayment$', views.goaddcustpayment, name='goaddcustpayment'),
    re_path(r'^customerspayment$', views.customerspayment, name='customerspayment'),
    re_path(r'^goaddcustestimate$', views.goaddcustestimate, name='goaddcustestimate'),
    re_path(r'^customersestimate$', views.customersestimate, name='customersestimate'),
    re_path(r'^goaddcustsalrecpt$', views.goaddcustsalrecpt, name='goaddcustsalrecpt'),
    re_path(r'^customerssalrecpt$', views.customerssalrecpt, name='customerssalrecpt'),
    re_path(r'^goaddcustcreditnote$', views.goaddcustcreditnote, name='goaddcustcreditnote'),
    re_path(r'^customerscreditnote$', views.customerscreditnote, name='customerscreditnote'),
    re_path(r'^goaddcustdelchrg$', views.goaddcustdelchrg, name='goaddcustdelchrg'),
    re_path(r'^customersdelchrg$', views.customersdelchrg, name='customersdelchrg'),
    re_path(r'^goaddcusttimeact$', views.goaddcusttimeact, name='goaddcusttimeact'),
    re_path(r'^customerstimeact$', views.customerstimeact, name='customerstimeact'),
    re_path(r'^supplierstimeact$', views.supplierstimeact, name='supplierstimeact'),
    re_path(r'^suppacttime$', views.suppacttime, name='suppacttime'),

    re_path(r'^get_data$', views.getdata, name='getdata'),
    re_path(r'^get_data1$', views.getdata1, name='getdata1'),
    re_path(r'^get_item$', views.getitems, name='getitems'),
    re_path(r'^getbalan$', views.getbalan, name='getbalan'),
    re_path(r'^getinvpro$', views.getinvpro, name='getinvpro'),
    re_path(r'^getterm$', views.getterm, name='getterm'),

    re_path(r'^gooexpensesuppliers$', views.gooexpensesuppliers, name='gooexpensesuppliers'),
    re_path(r'^expensesupplier$', views.expensesupplier, name='expensesupplier'),
    re_path(r'^gooexpensecustomer$', views.gooexpensecustomer, name='gooexpensecustomer'),
    re_path(r'^expensecustomers$', views.expensecustomers, name='expensecustomers'),

    re_path(r'^getitempay$', views.getitempay, name='getitempay'),
    re_path(r'^get_supdata$', views.getsuppdata, name='getsuppdata'),
    re_path(r'^get_supitems$', views.getsupitems, name='getsupitems'),

    re_path(r'^getsuppdata1$', views.getsuppdata1, name='getsuppdata1'),
    re_path(r'^getsuppitems$', views.getsuppitems, name='getsuppitems'),
    re_path(r'^getsuppcustdata$', views.getsuppcustdata, name='getsuppcustdata'),

    re_path(r'^goaddsuppliersbill$', views.goaddsuppliersbill, name='goaddsuppliersbill'),
    re_path(r'^goaddsuppliercredit$', views.goaddsuppliercredit, name='goaddsuppliercredit'),

    re_path(r'^suppliercreatebill$', views.suppliercreatebill, name='suppliercreatebill'),
    re_path(r'^suppliercreatecredit$', views.suppliercreatecredit, name='suppliercreatecredit'),

    re_path(r'^goaddsupplierscheque$', views.goaddsupplierscheque, name='goaddsupplierscheque'),
    re_path(r'^suppliercreatecheque$', views.suppliercreatecheque, name='suppliercreatecheque'),
    re_path(r'^gocustomerscheque$', views.gocustomerscheque, name='gocustomerscheque'),
    re_path(r'^customerscheque$', views.customerscheque, name='customerscheque'),

    re_path(r'^gocoa/suppliercoacreate$', views.suppliercoacreate, name='suppliercoacreate'),
    re_path(r'^gocoa/supplieracccreate$', views.supplieracccreate, name='supplieracccreate'),
    re_path(r'^gocoa/paymentcoacreate$', views.paymentcoacreate, name='paymentcoacreate'),
    re_path(r'^gocoa/paymentacccreate$', views.paymentacccreate, name='paymentacccreate'),
    re_path(r'^gocoa/salrecptcoacreate$', views.salrecptcoacreate, name='salrecptcoacreate'),
    re_path(r'^gocoa/salrecptacccreate$', views.salrecptacccreate, name='salrecptacccreate'),
    re_path(r'^gocoa/editsalrecptcoacreate$', views.editsalrecptcoacreate, name='editsalrecptcoacreate'),
    re_path(r'^gocoa/editsalrecptacccreate$', views.editsalrecptacccreate, name='editsalrecptacccreate'),
    re_path(r'^gocoa/productcoacreate$', views.productcoacreate, name='productcoacreate'),
    re_path(r'^gocoa/product1coacreate$', views.product1coacreate, name='product1coacreate'),
    re_path(r'^gocoa/product2coacreate$', views.product2coacreate, name='product2coacreate'),
    re_path(r'^gocoa/productacccreate$', views.productacccreate, name='productacccreate'),
    re_path(r'^gocoa/noninvcoacreate$', views.noninvcoacreate, name='noninvcoacreate'),
    re_path(r'^gocoa/noninvcoacreate1$', views.noninvcoacreate1, name='noninvcoacreate1'),
    re_path(r'^gocoa/noninvacccreate$', views.noninvacccreate, name='noninvacccreate'),
    re_path(r'^gocoa/sercoacreate$', views.sercoacreate, name='sercoacreate'),
    re_path(r'^gocoa/seracccreate$', views.seracccreate, name='seracccreate'),
    re_path(r'^gocoa/expencoacreate$', views.expencoacreate, name='expencoacreate'),
    re_path(r'^gocoa/expenacccreate$', views.expenacccreate, name='expenacccreate'),

    re_path(r'^repay$', views.repay, name='repay'),
    re_path(r'^goofflinebank2$', views.goofflinebank2, name='goofflinebank2'),
    re_path(r'^addbalance$', views.addbalance, name='addbalance'),
    re_path(r'^uploadstatement$', views.uploadstatement, name='uploadstatement'),
    re_path(r'^addbankdata/(?P<bankstatementid>\d+)$', views.addbankdata, name='addbankdata'),
    re_path(r'^addtoaccounts$', views.addtoaccounts, name='addtoaccounts'),

    re_path(r'^profitandloss$', views.profitandloss, name='profitandloss'),
    re_path(r'^profitandloss1$', views.profitandloss1, name='profitandloss1'),
    re_path(r'^profitandlossfilter$', views.profitandlossfiltered, name='profitandlossfilter'),
    re_path(r'^balancesheet$', views.balancesheet, name='balancesheet'),
    re_path(r'^balancesheet1$', views.balancesheet1, name='balancesheet1'),
    re_path(r'^balancesheet2$', views.balancesheet2, name='balancesheet2'),
    re_path(r'^balancesheetfilter$', views.balancesheetfiltered, name='balancesheetfilter'),
    re_path(r'^accreceivables$', views.accreceivables, name='accreceivables'),
    re_path(r'^accreceivables1$', views.accreceivables1, name='accreceivables1'),
    re_path(r'^accpayables$', views.accpayables, name='accpayables'),
    re_path(r'^accpayables1$', views.accpayables1, name='accpayables1'),
    re_path(r'^customisereport$', views.customisereport, name='customisereport'),
    re_path(r'^runreport/(?P<accounts1id>\d+)$', views.runreport, name='runreport'),
    re_path(r'^runreports/(?P<accountsid>\d+)$', views.runreports, name='runreports'),
    re_path(r'^runreportfiltered/(?P<accounts1id>\d+)$', views.runreportfiltered, name='runreportfiltered'),
    re_path(r'^runreportfilterednew/(?P<accountsid>\d+)$', views.runreportfilterednew, name='runreportfilterednew'),

    re_path(r'^cashposition', views.cashposition, name='cashposition'),
    re_path(r'^updateaccounts',views.updateaccounts,name='updateaccounts'),
    re_path(r'^editaccounts',views.editaccounts,name='editaccounts'),
    re_path(r'^billingandsub',views.gobillingandsub,name='gobillingandsub'),
    re_path(r'^goaccountexpense',views.goaccountexpense,name='goaccountexpense'),
    re_path(r'^goaccountsales',views.goaccountsales,name='goaccountsales'),

    re_path(r'^customstyle',views.customstyle,name='customstyle'),
    re_path(r'^newstyle',views.newstyle,name='newstyle'),
    re_path(r'^addnewstyle',views.addnewstyle,name='addnewstyle'),
    re_path(r'^editstyle/(?P<customizeid>\d+)$',views.editstyle,name='editstyle'),
    re_path(r'^editstyle/updatestyle/(?P<customizeid>\d+)$',views.updatestyle,name='updatestyle'),
    re_path(r'^deletestyle/(?P<customizeid>\d+)$',views.deletestyle,name='deletestyle'),




    # Ananthakrishnan
    
    re_path(r'^gosearch',views.gosearch,name='gosearch'),

    path('cust_add_file/<int:id>',views.cust_add_file,name='cust_add_file'),

    path('gocustomers', views.gocustomers, name='gocustomers'),

    path('gocustomers1',views.gocustomers1,name='gocustomers1'),

    path('gocustomers2',views.gocustomers2,name='gocustomers2'),

    

    path('gstverification',views.gstverification,name='gstverification'),

    path('customer_profile/<int:id>',views.customer_profile,name='customer_profile'),

    

    path('goestimate',views.goestimate,name='goestimate'),

    path('estindex2',views.estindex2,name='estindex2'),

    path('estcreate2',views.estcreate2,name='estcreate2'),

    path('new_customers',views.new_customers,name='new_customers'),

    path('estimate_create_item',views.estimate_create_item,name='estimate_create_item'),

    path('estimate_create_item2/<int:id>',views.estimate_create_item2,name='estimate_create_item2'),

     path('new_customers4/<int:id>',views.new_customers4,name='new_customers4'),


    

    path('updateestimate2/<int:id>',views.updateestimate2,name='updateestimate2'),

    path('search_estimate',views.search_estimate,name='search_estimate'),

    path('estimate_view/<int:id>',views.estimate_view,name='estimate_view'),

    path('convert1/<int:id>',views.convert1,name='convert1'),

    path('convert2/<int:id>',views.convert2,name='convert2'),

    path('estmate_filter1',views.estmate_filter1,name='estmate_filter1'),

    path('estmate_filter2',views.estmate_filter2,name='estmate_filter2'),

    path('estmate_filter3',views.estmate_filter3,name='estmate_filter3'),

    path('estimate_pdf',views.estimate_pdf,name='estimate_pdf'),

    path('new_customers1',views.new_customers1,name='new_customers1'),


    
     


    # Sales

    path('gosalesorder',views.gosalesorder,name='gosalesorder'),

    path('newsalesorder',views.newsalesorder,name='newsalesorder'),

    path('createsales_record',views.createsales_record,name='createsales_record'),

    path('new_customers2',views.new_customers2,name='new_customers2'),

    path('sales_order_view/<int:id>',views.sales_order_view,name='sales_order_view'),

    path('sales_order_delete/<int:id>',views.sales_order_delete,name='sales_order_delete'),

    path('edit_sales_order/<int:id>',views.edit_sales_order,name='edit_sales_order'),

    path('updatesale/<int:id>',views.updatesale,name='updatesale'),

    path('sale_convert1/<int:id>',views.sale_convert1,name='sale_convert1'),

    path('sale_convert2/<int:id>',views.sale_convert2,name='sale_convert2'),

    path('sale_filter1',views.sale_filter1,name='sale_filter1'),

    path('sale_filter2',views.sale_filter2,name='sale_filter2'),

    path('sale_filter3',views.sale_filter3,name='sale_filter3'),

    path('search_sale',views.search_sale,name='search_sale'),

    path('invoice_view/<int:id>',views.invoice_view,name='invoice_view'),
    path('render_pdfinvoice_view/<int:id>',views.render_pdfinvoice_view,name='render_pdfinvoice_view'),
    path('new_customers3',views.new_customers3,name='new_customers3'),

    path('sale_create_item',views.sale_create_item,name='sale_create_item'),

    


    # invoice

    re_path(r'^goinvoices$', views.goinvoices, name='goinvoices'),
    re_path(r'^goaddinvoices$', views.goaddinvoices, name='goaddinvoices'),
    re_path(r'^editinvoice/(?P<id>\d+)$', views.editinvoice, name='editinvoice'),
    path('deleteinvoice/<int:id>',views.deleteinvoice,name='deleteinvoice'),
    re_path(r'^editinvoice/updateinvoice/(?P<id>\d+)$', views.updateinvoice, name='updateinvoice'),
    path('invoice_status/<int:id>',views.invoice_status,name='invoice_status'),

    path('inv_create_item',views.inv_create_item,name='inv_create_item'),

    path('updateinvoice2/<int:id>',views.updateinvoice2,name='updateinvoice2'),

    
    
    path('invcreate2',views.invcreate2,name='invcreate2'),
    path('goinvoices1',views.goinvoices1,name='goinvoices1'),

    path('goinvoices2',views.goinvoices2,name='goinvoices2'),

    path('goinvoices3',views.goinvoices3,name='goinvoices3'),

    

    # receipt

    
    path('gopayment_received',views.gopayment_received,name='gopayment_received'),
    path('payment_received',views.payment_received,name='payment_received'),

    path('getdatainv',views.getdatainv,name='getdatainv'),

    path('paymentcreate2',views.paymentcreate2,name='paymentcreate2'),

    path('search_payment_received',csrf_exempt(views.search_payment_received),name='search_payment_received'),

    path('payment_view/<int:id>',views.payment_view,name='payment_view'),

    path('edit_payment/<int:id>',views.edit_payment,name='edit_payment'),

    path('edit_payment2/<int:id>',views.edit_payment2,name='edit_payment2'),

    

    

    path('delete_payment/<int:id>',views.delete_payment,name='delete_payment'),

    path('search_resept/<int:id>',views.search_resept,name='search_resept'),

    path('account_transactions/<int:id>',views.account_transactions,name='account_transactions'),

    path('account_transactions1',views.account_transactions1,name='account_transactions1'),

    path('getitems2',views.getitems2,name='getitems2'),


    path('estimate_add_file/<int:id>',views.estimate_add_file,name='estimate_add_file'),

    path('sales_add_file/<int:id>',views.sales_add_file,name='sales_add_file'),

    path('invoice_add_file/<int:id>',views.invoice_add_file,name='invoice_add_file'),

    path('update_opening_balance/<int:id>',views.update_opening_balance,name='update_opening_balance'),

    path('gstr11',views.gstr11,name='gstr11'),


    
    

    


   
    


    


    


    


    
    

    # path('pdf',views.pdf,name='pdf'),





    # Rahanas ----------

    # item
    re_path(r'^add_item$', views.add_item, name='add_item'),
    re_path(r'^add_unit$', views.add_unit, name='add_unit'),
    re_path(r'^goitem$', views.goitem, name='goitem'),
    re_path(r'^create_item$', views.create_item, name='create_item'),
    re_path(r'^deleteitem/(?P<id>\d+)$', views.deleteitem, name='deleteitem'),
    #re_path(r'^showservices$', views.showservices, name='showservices'),
    re_path(r'^create_unit$', views.create_unit, name='create_unit'),
    re_path(r'^view_item/(?P<id>\d+)$', views.view_item, name='view_item'),
    re_path(r'^itemedit_page/(?P<id>\d+)$', views.itemedit_page, name='itemedit_page'),
    re_path(r'^igoods$', views.igoods, name='igoods'),
    re_path(r'^iservices$', views.iservices, name='iservices'),
    re_path(r'^iordername$', views.iordername, name='iordername'),
    re_path(r'^iodhsn$', views.iodhsn, name='iodhsn'),
    re_path(r'^iactive$', views.iactive, name='iactive'),
    re_path(r'^inactive$', views.inactive, name='inactive'),
    re_path(r'^ipurchase$', views.ipurchase, name='ipurchase'),
    re_path(r'^isales$', views.isales, name='isales'),
    re_path(r'^update_item/(?P<id>\d+)$', views.update_item, name='update_item'),
    re_path(r'^iod_rate$', views.iod_rate, name='iod_rate'),
    re_path(r'^iod_import$', views.iod_import, name='iod_import'),
    re_path(r'^iod_export$', views.iod_export, name='iod_export'),

    #  manual journal
    re_path(r'^gomjoural$', views.gomjoural, name='gomjoural'),
    re_path(r'^add_mjournal$', views.add_mjournal, name='add_mjournal'),
    re_path(r'^create_mjournal$', views.create_mjournal, name='create_mjournal'),
    re_path(r'^view_mj/(?P<id>\d+)$', views.view_mj, name='view_mj'),
    re_path(r'^mj_edit_page/(?P<id>\d+)$', views.mj_edit_page, name='mj_edit_page'),
    re_path(r'^update_mj/(?P<id>\d+)$', views.update_mj, name='update_mj'),
    re_path(r'^deletemj/(?P<id>\d+)$', views.deletemj, name='deletemj'),
    re_path(r'^mjdraft$', views.mjdraft, name='mjdraft'),
    re_path(r'^mjpublish$', views.mjpublish, name='mjpublish'),

    #   settings
    re_path(r'^C_profile$', views.C_profile, name='C_profile'),
    re_path(r'^update_cprofile$', views.update_cprofile, name='update_cprofile'),
    re_path(r'^view_users$', views.view_users, name='view_users'),
    re_path(r'^Currencies$', views.Currencies, name='Currencies'),
    re_path(r'^create_currency$', views.create_currency, name='create_currency'),
    re_path(r'^gotemplates$', views.gotemplates, name='gotemplates'),
    re_path(r'^temp_inv$', views.temp_inv, name='temp_inv'),
    re_path(r'^addcurrencies$', views.addcurrencies, name='addcurrencies'),
    re_path(r'^edit_currencies/(?P<id>\d+)$', views.edit_currencies, name='edit_currencies'),
    re_path(r'^update_currency/(?P<id>\d+)$', views.update_currency, name='update_currency'),
    re_path(r'^delete_currency/(?P<id>\d+)$', views.delete_currency, name='delete_currency'),
    re_path(r'^temp_est$', views.temp_est, name='temp_est'),



    re_path(r'^gotemplates$', views.gotemplates, name='gotemplates'),
    re_path(r'^temp_inv$', views.temp_inv, name='temp_inv'),
    re_path(r'^temp_est$', views.temp_est, name='temp_est'),
    re_path(r'^temp_payrec$',views.temp_payrec,name='temp_payrec'),
    re_path(r'^temp_vendpay$',views.temp_vendpay,name='temp_vendpay'),
    re_path(r'^temp_custst$',views.temp_custst,name='temp_custst'),
    re_path(r'^temp_vendst$',views.temp_vendst,name='temp_vendst'),
    re_path(r'^temp_deliveryc$',views.temp_deliveryc,name='temp_deliveryc'),
    re_path(r'^temp_creditnote$',views.temp_creditnote,name='temp_creditnote'),
    re_path(r'^temp_salesorder$',views.temp_salesorder,name='temp_salesorder'),
    re_path(r'^temp_purchaseorder$',views.temp_purchaseorder,name='temp_purchaseorder'),
    re_path(r'^temp_vendorcredit$',views.temp_vendorcredit,name='temp_vendorcredit'),
    re_path(r'^temp_journal$',views.temp_journal,name='temp_journal'),
    re_path(r'^temp_bill$',views.temp_bill,name='temp_bill'),


    re_path(r'^item_trans/(?P<id>\d+)$',views.item_trans,name='item_trans'),
    re_path(r'^gostock_adjust$', views.gostock_adjust, name='gostock_adjust'),
    re_path(r'^stock_adjustpage$', views.stock_adjustpage, name='stock_adjustpage'),
    re_path(r'^getit$', views.getit, name='getit'),
    re_path(r'^create_reason$', views.create_reason, name='create_reason'),
    re_path(r'^create_stock_adjustment$', views.create_stock_adjustment, name='create_stock_adjustment'),
    re_path(r'^view_stockadjust/(?P<id>\d+)$',views.view_stockadjust,name='view_stockadjust'),
    re_path(r'^edit_stockadjust/(?P<id>\d+)$',views.edit_stockadjust,name='edit_stockadjust'),
    re_path(r'^update_stock_adjustment/(?P<id>\d+)$',views.update_stock_adjustment,name='update_stock_adjustment'),
    re_path(r'^stocksummary$', views.stocksummary, name='stocksummary'),
    re_path(r'^stocksummary1$', views.stocksummary1, name='stocksummary1'),
    re_path(r'^stockvaluation$', views.stockvaluation, name='stockvaluation'),
    re_path(r'^stockvaluation1$', views.stockvaluation1, name='stockvaluation1'),
    re_path(r'^deletestockadjust/(?P<id>\d+)$', views.deletestockadjust, name='deletestockadjust'),
    re_path(r'^saf_quandity$', views.saf_quandity, name='saf_quandity'),
    re_path(r'^saf_value$', views.saf_value, name='saf_value'),

    
    re_path(r'^gstr1$', views.gstr1, name='gstr1'),
    re_path(r'^gstr3b$', views.gstr3b, name='gstr3b'),
    re_path(r'^gstr3b1$', views.gstr3b1, name='gstr3b1'),

    re_path(r'^goewaybill$', views.goewaybill, name='goewaybill'),
    re_path(r'^addewaybill/(?P<id>\d+)$', views.addewaybill, name='addewaybill'),
    re_path(r'^create_transporter$', views.create_transporter, name='create_transporter'),
    re_path(r'^create_eway_inv$', views.create_eway_inv, name='create_eway_inv'),
    re_path(r'^view_eway_inv$', views.view_eway_inv, name='view_eway_inv'),
    

    #Jisha

    re_path(r'^govendor$',views.govendor,name='govendor'),
    re_path(r'^vendor_active$',views.vendor_active,name='vendor_active'),
    re_path(r'^vendor_inactive$',views.vendor_inactive,name='vendor_inactive'),
    re_path(r'^addvendor$',views.addvendor,name='addvendor'),
    re_path(r'^createvendor$',views.createvendor,name='createvendor'),
    re_path(r'^viewvendor/(?P<id>\d+)$', views.viewvendor, name='viewvendor'),
    # re_path(r'^viewvendor/viewvendor1/(?P<id>\d+)$', views.viewvendor1, name='viewvendor1'),
    re_path(r'^goeditvendor/(?P<id>\d+)$', views.goeditvendor, name='goeditvendor'),
    re_path(r'^goeditvendor/editvendor/(?P<id>\d+)$', views.editvendor, name='editvendor'),
    re_path(r'^deletevendor/(?P<id>\d+)$', views.deletevendor, name='deletevendor'),

    re_path(r'^createvendor1$',views.createvendor1,name='createvendor1'),
    re_path(r'^createvendor2$',views.createvendor2,name='createvendor2'),
    re_path(r'^createvendor3$',views.createvendor3,name='createvendor3'),
    re_path(r'^createvendor4$',views.createvendor4,name='createvendor4'),

    re_path(r'^createcustomer1$', views.createcustomer1, name='createcustomer1'),
    re_path(r'^createcustomer2$', views.createcustomer2, name='createcustomer2'),
    re_path(r'^createcustomer3$', views.createcustomer3, name='createcustomer3'),

    re_path(r'^create_item1$',views.create_item1,name='create_item1'),
    re_path(r'^create_item2$',views.create_item2,name='create_item2'),
    re_path(r'^create_item3$',views.create_item3,name='create_item3'),

    re_path(r'^create_unit1$',views.create_unit1,name='create_unit1'),

    re_path(r'^getvendordata$',views.getvendordata,name='getvendordata'),
    re_path(r'^getperiod$',views.getperiod,name='getperiod'),

    re_path(r'^gopurchaseorder$',views.gopurchaseorder,name='gopurchaseorder'),
    re_path(r'^addpurchaseorder$',views.addpurchaseorder,name='addpurchaseorder'),
    re_path(r'^createpurchaseorder$',views.createpurchaseorder,name='createpurchaseorder'),
    re_path(r'^viewpurchaseorder/(?P<id>\d+)$',views.viewpurchaseorder,name='viewpurchaseorder'),
    re_path(r'^viewpurchaseorder/goeditpurchaseorder/(?P<id>\d+)$',views.goeditpurchaseorder,name='goeditpurchaseorder'),
    re_path(r'^viewpurchaseorder/deletepurchasorder/(?P<id>\d+)$', views.deletepurchasorder, name='deletepurchasorder'),
    re_path(r'^viewpurchaseorder/goeditpurchaseorder/editpurchaseorder/(?P<id>\d+)$', views.editpurchaseorder, name='editpurchaseorder'),

    re_path(r'^convertapproved/(?P<id>\d+)$',views.convertapproved,name='convertapproved'),
    re_path(r'^convertbilled/(?P<id>\d+)$',views.convertbilled,name='convertbilled'),

    re_path(r'^getdata2$',views.getdata2,name='getdata2'),   

    re_path(r'^gobilling$',views.gobilling,name='gobilling'),
    re_path(r'^addbilling$',views.addbilling,name='addbilling'),
    re_path(r'^createbill$',views.createbill,name='createbill'),
    re_path(r'^viewbill/(?P<id>\d+)$',views.viewbill,name='viewbill'),
    re_path(r'^viewbill/deletebill/(?P<id>\d+)$',views.deletebill,name='deletebill'),
    re_path(r'^billconvert/(?P<id>\d+)$',views.billconvert,name='billconvert'),
    re_path(r'^viewbill/goeditbill/(?P<id>\d+)$',views.goeditbill,name='goeditbill'),
    re_path(r'^viewbill/goeditbill/editpurchasebill/(?P<id>\d+)$',views.editpurchasebill,name='editpurchasebill'),

    re_path(r'^goexpenses$',views.goexpenses,name='goexpenses'),
    re_path(r'^addexpenses$',views.addexpenses,name='addexpenses'),
    re_path(r'^createexpense$',views.createexpense,name='createexpense'),
    re_path(r'^viewexpense/(?P<id>\d+)$',views.viewexpense,name='viewexpense'),
    re_path(r'^goeditexpense/(?P<id>\d+)$',views.goeditexpense,name='goeditexpense'),
    re_path(r'^goeditexpense/editexpense/(?P<id>\d+)$',views.editexpense,name='editexpense'),
    re_path(r'^deleteexpense/(?P<id>\d+)$', views.deleteexpense, name='deleteexpense'),

    re_path(r'^credit_period$', views.credit_period, name='credit_period'),
    re_path(r'^credit_period1$', views.credit_period1, name='credit_period1'),
    re_path(r'^credit_period2$', views.credit_period2, name='credit_period2'),
    re_path(r'^credit_period3$', views.credit_period3, name='credit_period3'),
    re_path(r'^credit_period4$', views.credit_period4, name='credit_period4'),

    re_path(r'^porder_draft$', views.porder_draft, name='porder_draft'),
    re_path(r'^porder_billed$', views.porder_billed, name='porder_billed'),
    re_path(r'^porder_approved$', views.porder_approved, name='porder_approved'),
    re_path(r'^bill_draft$', views.bill_draft, name='bill_draft'),
    re_path(r'^bill_billed$', views.bill_billed, name='bill_billed'),

    re_path(r'^getbilldata$', views.getbilldata, name='getbilldata'),

    re_path(r'^gopurchasepymnt$', views.gopurchasepymnt, name='gopurchasepymnt'),
    re_path(r'^addpurchasepymnt$', views.addpurchasepymnt, name='addpurchasepymnt'),
    re_path(r'^createpurchasepymnt$', views.createpurchasepymnt, name='createpurchasepymnt'),
    re_path(r'^viewpurchasepymnt/(?P<id>\d+)$', views.viewpurchasepymnt, name='viewpurchasepymnt'),
    re_path(r'^viewpurchasepymnt/goeditpurchasepymnt/(?P<id>\d+)$', views.goeditpurchasepymnt, name='goeditpurchasepymnt'),
    re_path(r'^viewpurchasepymnt/goeditpurchasepymnt/editpurchasepymnt/(?P<id>\d+)$', views.editpurchasepymnt, name='editpurchasepymnt'),
    re_path(r'^viewpurchasepymnt/deletepurchasepymnt/(?P<id>\d+)$', views.deletepurchasepymnt, name='deletepurchasepymnt'),

    re_path(r'^gopurchasedebit$', views.gopurchasedebit, name='gopurchasedebit'),
    re_path(r'^addpurchasedebit$', views.addpurchasedebit, name='addpurchasedebit'),
    re_path(r'^createpurchasedebit$', views.createpurchasedebit, name='createpurchasedebit'),
    re_path(r'^viewpurchasedebit/(?P<id>\d+)$', views.viewpurchasedebit, name='viewpurchasedebit'),
    re_path(r'^viewpurchasedebit/goeditpurchasedebit/(?P<id>\d+)$', views.goeditpurchasedebit, name='goeditpurchasedebit'),
    re_path(r'^viewpurchasedebit/goeditpurchasedebit/editpurchasedebit/(?P<id>\d+)$', views.editpurchasedebit, name='editpurchasedebit'),
    re_path(r'^viewpurchasedebit/deletepurchasedebit/(?P<id>\d+)$', views.deletepurchasedebit, name='deletepurchasedebit'),

    re_path(r'^bill_add_file/(?P<id>\d+)$', views.bill_add_file, name='bill_add_file'),
    re_path(r'^porder_add_file/(?P<id>\d+)$', views.porder_add_file, name='porder_add_file'),
    re_path(r'^expense_add_file/(?P<id>\d+)$', views.expense_add_file, name='expense_add_file'),

    path('purchase_acctransactions/<str:id>',views.purchase_acctransactions,name='purchase_acctransactions'),
    path('purchase_acctransactions1',views.purchase_acctransactions1,name='purchase_acctransactions1'),

    path('trial_balance', views.trial_balance, name='trial_balance'),
    path('trial_balance1', views.trial_balance1, name='trial_balance1'),
    path('plreport/<str:id>', views.plreport, name='plreport'), 
    path('plreport_flt/<int:id>', views.plreport_flt, name='plreport_flt'),
    path('bsreport/<str:id>', views.bsreport, name='bsreport'),
    path('tbreport/<str:id>', views.tbreport, name='tbreport'),
    path('streport/<str:id>', views.streport, name='streport'),
    path('stkvalreport/<str:id>', views.stkvalreport, name='stkvalreport'),

    re_path(r'^demo$', views.demo, name='demo'),
    re_path(r'^itemdata$', views.itemdata, name='itemdata'),
    
    re_path(r'^payment_method$', views.payment_method, name='payment_method'),
    re_path(r'^createaccount1$', views.createaccount1, name='createaccount1'),
    re_path(r'^createaccount2$', views.createaccount2, name='createaccount2'),

    re_path(r'^bnnk',views.bnnk,name='bnnk'),
    re_path(r'^bnk1/(?P<pk>\d+)$',views.bnk1,name='bnk1'),
    re_path(r'^accpayment$',views.accpayment,name='accpayment'),
    re_path(r'^trial$',views.trial,name='trial'),
    re_path(r'^cras$',views.cras,name='cras'),
    
    re_path(r'^acre$',views.acre,name='acre'),
    re_path(r'^acres/(?P<pk>\d+)$',views.acres,name='acres'),
    re_path(r'^curli$',views.curli,name='curli'),
    re_path(r'^fix$',views.fix,name='fix'),
    re_path(r'^nonass$',views.nonass,name='nonass'),
    re_path(r'^accpay$',views.accpay,name='accpay'),
    re_path(r'^credc$',views.credc,name='credc'),
    re_path(r'^nonli$',views.nonli,name='nonli'),
    re_path(r'^eqt$',views.eqt,name='eqt'),
    re_path(r'^incm$',views.incm,name='incm'),
    re_path(r'^oincm$',views.oincm,name='oincm'),
    re_path(r'^cog$',views.cog,name='cog'),
    re_path(r'^exp$',views.exp,name='exp'),

    re_path(r'^add_expenses/(?P<pk>\d+)$',views.add_expenses,name='add_expenses'),
    re_path(r'^payment_vnk/(?P<pk>\d+)$',views.payment_vnk,name='payment_vnk'),
    re_path(r'^payment_vendor/(?P<pk>\d+)$',views.payment_vendor,name='payment_vendor'),
    re_path(r'^exp_view/(?P<pk>\d+)$',views.exp_view,name='exp_view'),
    re_path(r'^exp_edit/(?P<pk>\d+)$',views.exp_edit,name='exp_edit'),
    re_path(r'^deleteexp/(?P<pk>\d+)$',views.deleteexp,name='deleteexp'),
    re_path(r'^cus_view/(?P<pk>\d+)$',views.cus_view,name='cus_view'),
    re_path(r'^cus_edit/(?P<pk>\d+)$',views.cus_edit,name='cus_edit'),
    re_path(r'^deletecus/(?P<pk>\d+)$',views.deletecus,name='deletecus'),
    re_path(r'^vend_view/(?P<pk>\d+)$',views.vend_view,name='vend_view'),
    re_path(r'^vend_edit/(?P<pk>\d+)$',views.vend_edit,name='vend_edit'),
    re_path(r'^deletevend/(?P<pk>\d+)$',views.deletevend,name='deletevend'),
    path('bank_recon/<int:pk>', views.bank_recon, name='bank_recon'),
    path('start_reconcile/<int:pk>', views.start_reconcile, name='start_reconcile'), 
    path('gettermss/', views.gettermss, name='gettermss'),
    path('pym_acc_crt/', views.pym_acc_crt, name='pym_acc_crt'),
    path('paym_acc/', views.paym_acc, name='paym_acc'),
    path('active_cust/<int:pk>', views.active_cust, name='active_cust'),
    path('inactive_cust/<int:pk>', views.inactive_cust, name='inactive_cust'),
    path('credit_note/', views.credit_note, name='credit_note'),
    path('addpurchasecredit/', views.addpurchasecredit, name='addpurchasecredit'),
    path('getcustdata/', views.getcustdata, name='getcustdata'),
    path('create_credit/', views.create_credit, name='create_credit'),
    path('bnk_disables/<int:pk>', views.bnk_disables, name='bnk_disables'),
    path('delete_recon/<int:pk>', views.delete_recon, name='delete_recon'),
    path('render_pdfpayment_view/<int:id>', views.render_pdfpayment_view, name='render_pdfpayment_view'),
    path('render_pdfestimate_view/<int:id>', views.render_pdfestimate_view, name='render_pdfestimate_view'),
    path('render_pdfsalesorder_view/<int:id>', views.render_pdfsalesorder_view, name='render_pdfsalesorder_view'),
    path('render_pdfpurchase_view/<int:id>', views.render_pdfpurchase_view, name='render_pdfpurchase_view'),
    path('render_pdfbill_view/<int:id>', views.render_pdfbill_view, name='render_pdfbill_view'),

    path('render_pdfpurpym_view/<int:id>', views.render_pdfpurpym_view, name='render_pdfpurpym_view'),
    path('render_pdfdebit_view/<int:id>', views.render_pdfdebit_view, name='render_pdfdebit_view'),
    path('viewcredit/<int:id>', views.viewcredit, name='viewcredit'),
    path('render_pdf_credit/<int:id>', views.render_pdf_credit, name='render_pdf_credit'),
    path('editcreditnote/<int:id>', views.editcreditnote, name='editcreditnote'),
    path('deletecredit/<int:id>', views.deletecredit, name='deletecredit'),
    path('editcreditfun/<int:id>', views.editcreditfun, name='editcreditfun'),
    re_path(r'^remove$', views.remove, name='remove'),
    re_path(r'^removepbill$', views.removepbill, name='removepbill'),
    re_path(r'^removedebit$', views.removedebit, name='removedebit'),
    re_path(r'^removeesti$', views.removeesti, name='removeesti'),
    re_path(r'^removesales$', views.removesales, name='removesales'),
    re_path(r'^removeinv$', views.removeinv, name='removeinv'),

    
 

    
      # Forgot Password --------- 07-01-23 Shebin Shaji
        path('Forgote-Password',views.password_change,name='password_change'),
        path('Email-check',views.forgot_password,name='forgot_password'),
        path('Set-Password',views.change_to_new_password,name='change_to_new_password'),
        
    
]
