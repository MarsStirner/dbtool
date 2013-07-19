#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

__doc__ = '''\
- Добавлена куча таблиц справочников
'''

def upgrade(conn):
    global config        
    c = conn.cursor()
    
    sql = u'''
DROP TABLE IF EXISTS `rb_F001_Tfoms`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_F001_Tfoms` (
  `tf_kod` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `d_edit` date DEFAULT NULL,
  `d_end` date DEFAULT NULL,
  `e_mail` varchar(255) DEFAULT NULL,
  `fam_dir` varchar(255) DEFAULT NULL,
  `fax` varchar(255) DEFAULT NULL,
  `idx` varchar(255) DEFAULT NULL,
  `im_dir` varchar(255) DEFAULT NULL,
  `kf_tf` bigint(20) DEFAULT NULL,
  `name_tfk` varchar(255) DEFAULT NULL,
  `name_tfp` varchar(255) DEFAULT NULL,
  `ot_dir` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `tf_ogrn` varchar(255) DEFAULT NULL,
  `tf_okato` varchar(255) DEFAULT NULL,
  `www` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`tf_kod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_F002_SMO`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_F002_SMO` (
  `smocod` varchar(255) NOT NULL,
  `addr_f` varchar(255) DEFAULT NULL,
  `addr_j` varchar(255) DEFAULT NULL,
  `d_begin` date DEFAULT NULL,
  `d_edit` date DEFAULT NULL,
  `d_end` date DEFAULT NULL,
  `d_start` date DEFAULT NULL,
  `data_e` date DEFAULT NULL,
  `duved` date DEFAULT NULL,
  `e_mail` varchar(255) DEFAULT NULL,
  `fam_ruk` varchar(255) DEFAULT NULL,
  `fax` varchar(255) DEFAULT NULL,
  `im_ruk` varchar(255) DEFAULT NULL,
  `index_f` varchar(255) DEFAULT NULL,
  `index_j` varchar(255) DEFAULT NULL,
  `inn` varchar(255) DEFAULT NULL,
  `kol_zl` bigint(20) DEFAULT NULL,
  `kpp` varchar(255) DEFAULT NULL,
  `n_doc` varchar(255) DEFAULT NULL,
  `nal_p` varchar(255) DEFAULT NULL,
  `nam_smok` varchar(255) DEFAULT NULL,
  `nam_smop` varchar(255) DEFAULT NULL,
  `name_e` varchar(255) DEFAULT NULL,
  `ogrn` varchar(255) DEFAULT NULL,
  `okopf` varchar(255) DEFAULT NULL,
  `org` bigint(20) DEFAULT NULL,
  `ot_ruk` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `tf_okato` varchar(255) DEFAULT NULL,
  `www` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`smocod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_F003_MO`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_F003_MO` (
  `mcod` varchar(255) NOT NULL,
  `addr_j` varchar(255) DEFAULT NULL,
  `d_begin` date DEFAULT NULL,
  `d_edit` date DEFAULT NULL,
  `d_end` date DEFAULT NULL,
  `d_start` date DEFAULT NULL,
  `data_e` date DEFAULT NULL,
  `duved` date DEFAULT NULL,
  `e_mail` varchar(255) DEFAULT NULL,
  `fam_ruk` varchar(255) DEFAULT NULL,
  `fax` varchar(255) DEFAULT NULL,
  `im_ruk` varchar(255) DEFAULT NULL,
  `index_j` varchar(255) DEFAULT NULL,
  `inn` varchar(255) DEFAULT NULL,
  `kpp` varchar(255) DEFAULT NULL,
  `lpu` int(11) DEFAULT NULL,
  `mp` varchar(255) DEFAULT NULL,
  `n_doc` varchar(255) DEFAULT NULL,
  `nam_mok` varchar(255) DEFAULT NULL,
  `nam_mop` varchar(255) DEFAULT NULL,
  `name_e` varchar(255) DEFAULT NULL,
  `ogrn` varchar(255) DEFAULT NULL,
  `okopf` varchar(255) DEFAULT NULL,
  `org` bigint(20) DEFAULT NULL,
  `ot_ruk` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `tf_okato` varchar(255) DEFAULT NULL,
  `vedpri` bigint(20) DEFAULT NULL,
  `www` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`mcod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_F007_Vedom`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_F007_Vedom` (
  `idved` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `vedname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idved`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_F008_TipOMS`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_F008_TipOMS` (
  `iddoc` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `docname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`iddoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_F009_StatZL`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_F009_StatZL` (
  `idstatus` varchar(255) NOT NULL DEFAULT '',
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `statusname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idstatus`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_F010_Subekti`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_F010_Subekti` (
  `kod_tf` varchar(255) NOT NULL DEFAULT '',
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `kod_okato` varchar(255) DEFAULT NULL,
  `okrug` bigint(20) DEFAULT NULL,
  `subname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`kod_tf`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_F011_Tipdoc`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_F011_Tipdoc` (
  `iddoc` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `docname` varchar(255) DEFAULT NULL,
  `docnum` varchar(255) DEFAULT NULL,
  `docser` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`iddoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_F015_FedOkr`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_F015_FedOkr` (
  `kod_ok` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `okrname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`kod_ok`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_Kladr`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_Kladr` (
  `code` varchar(255) NOT NULL,
  `gninmb` varchar(255) DEFAULT NULL,
  `idx` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `ocatd` varchar(255) DEFAULT NULL,
  `socr` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `uno` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_KladrStreet`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_KladrStreet` (
  `code` varchar(255) NOT NULL,
  `gninmb` varchar(255) DEFAULT NULL,
  `idx` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `ocatd` varchar(255) DEFAULT NULL,
  `socr` varchar(255) DEFAULT NULL,
  `uno` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_M001_MKB10`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_M001_MKB10` (
  `idds` varchar(255) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `dsname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idds`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_O001_Oksm`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_O001_Oksm` (
  `kod` varchar(255) NOT NULL DEFAULT '',
  `alfa2` varchar(255) DEFAULT NULL,
  `alfa3` varchar(255) DEFAULT NULL,
  `data_upd` date DEFAULT NULL,
  `name11` varchar(255) DEFAULT NULL,
  `name12` varchar(255) DEFAULT NULL,
  `nomakt` varchar(255) DEFAULT NULL,
  `nomdescr` varchar(255) DEFAULT NULL,
  `status` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`kod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_O002_Okato`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_O002_Okato` (
  `ter` varchar(255) NOT NULL DEFAULT '',
  `centrum` varchar(255) DEFAULT NULL,
  `data_upd` date DEFAULT NULL,
  `kod1` varchar(255) DEFAULT NULL,
  `kod2` varchar(255) DEFAULT NULL,
  `kod3` varchar(255) DEFAULT NULL,
  `name1` varchar(255) DEFAULT NULL,
  `nomakt` varchar(255) DEFAULT NULL,
  `nomdescr` varchar(255) DEFAULT NULL,
  `razdel` varchar(255) DEFAULT NULL,
  `status` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`ter`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_O003_Okved`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_O003_Okved` (
  `kod` varchar(255) NOT NULL DEFAULT '',
  `data_upd` date DEFAULT NULL,
  `name11` varchar(255) DEFAULT NULL,
  `name12` varchar(255) DEFAULT NULL,
  `nomakt` varchar(255) DEFAULT NULL,
  `nomdescr` varchar(255) DEFAULT NULL,
  `prazdel` varchar(255) DEFAULT NULL,
  `razdel` varchar(255) DEFAULT NULL,
  `status` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`kod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_O004_Okfs`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_O004_Okfs` (
  `kod` varchar(255) NOT NULL DEFAULT '',
  `alg` varchar(255) DEFAULT NULL,
  `data_upd` date DEFAULT NULL,
  `name1` varchar(255) DEFAULT NULL,
  `nomakt` varchar(255) DEFAULT NULL,
  `status` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`kod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_O005_Okopf`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_O005_Okopf` (
  `kod` varchar(255) NOT NULL DEFAULT '',
  `alg` varchar(255) DEFAULT NULL,
  `data_upd` date DEFAULT NULL,
  `name1` varchar(255) DEFAULT NULL,
  `nomakt` varchar(255) DEFAULT NULL,
  `status` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`kod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V001_Nomerclr`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V001_Nomerclr` (
  `idrb` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `rbname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idrb`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V002_ProfOt`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V002_ProfOt` (
  `idpr` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `prname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idpr`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V003_LicUsl`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V003_LicUsl` (
  `idrl` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `ierarh` bigint(20) DEFAULT NULL,
  `licname` varchar(255) DEFAULT NULL,
  `prim` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`idrl`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V004_Medspec`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V004_Medspec` (
  `idmsp` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `mspname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idmsp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V005_Pol`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V005_Pol` (
  `idpol` bigint(20) NOT NULL,
  `polname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idpol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V006_UslMp`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V006_UslMp` (
  `idump` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `umpname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idump`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V007_NomMO`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V007_NomMO` (
  `idnmo` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `nmoname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idnmo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V008_VidMp`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V008_VidMp` (
  `idvmp` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `vmpname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idvmp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V009_Rezult`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V009_Rezult` (
  `idrmp` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `iduslov` bigint(20) DEFAULT NULL,
  `rmpname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idrmp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V010_Sposob`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V010_Sposob` (
  `idsp` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `spname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idsp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;    
'''
    c.execute(sql)
    
    sql = u'''
DROP TABLE IF EXISTS `rb_V012_Ishod`;
'''
    c.execute(sql)
    sql = u'''
CREATE TABLE IF NOT EXISTS `rb_V012_Ishod` (
  `idiz` bigint(20) NOT NULL,
  `datebeg` date DEFAULT NULL,
  `dateend` date DEFAULT NULL,
  `iduslov` bigint(20) DEFAULT NULL,
  `izname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`idiz`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
    c.execute(sql)
    
    
def downgrade(conn):
    pass