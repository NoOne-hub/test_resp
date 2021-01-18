import requests
import time



sess = requests.session()
# FruitShareCodes 东东农场
FruitShareCodes = ["93f99381e71140048b67dd3097891506", "15a2b0ab79e647509a07f59696b7b4e2","ca5e3106a24e42f3990da42f4f00c612","765a081119fe4dce917235b0109e29af","f06fd754304748369545872458d7149b"]
# PLANT_BEAN_SHARECODES 种豆得豆
PLANT_BEAN_SHARECODES = ["4npkonnsy7xi3ybp3mj7iss445oczfwvsm6um6y", "uwgpfl3hsfqp3wzzolvy5fpvvn3bdywjdgscvgi","k4fl7v7fvtmey7hgxjppoqbv6kec6zqrubku23q","7nk3uezyst2wyerel75ve5wxfu3h7wlwy7o5jii","cuted6op5h5atxahrk5oyiuye4"]
# DDFACTORY_SHARECODES 东东工厂 
DDFACTORY_SHARECODES = ["T0225KkcRxxN_AaEIhn1kfAIJgCjVWnYaS5kRrbA","T0205KkcHlxxpgaDfWyg_KFVCjVWnYaS5kRrbA","T018v_56QBca8V3SJR2b1ACjVWnYaS5kRrbA","T019-ak0EmhIgwuvVVKH7ZUCjVWnYaS5kRrbA", "T0117aWmwLbObt0CjVWnYaS5kRrbA"]

# JDZZ_SHARECODES 京东赚赚
JDZZ_SHARECODES = ["S5KkcRxxN_AaEIhn1kfAIJg","S5KkcHlxxpgaDfWyg_KFV","Sv_56QBca8V3SJR2b1A","S-ak0EmhIgwuvVVKH7ZU"]
# JDJOY_SHARECODES  疯狂joy
JDJOY_SHARECODES = ["pUl3fRSXb7Ko0s9aFjBfkat9zd5YaBeE","ClVWeUlyRAlf-tkrMjPAZQ==","U8JG4Hld01a5ZBe4TYLxNA==","FN3KqV95xi94ZMqbzq_1Wg==","Mx8YNQWT7hurfc3eWGgXhA=="]
# PETSHARECODES 东东萌宠
PETSHARECODES = ["MTAxODEyMjkyMDAwMDAwMDM5MzI3NTM3","MTE1NDUwMTI0MDAwMDAwMDM5MzQ0Njgx","MTE1NDUyMjEwMDAwMDAwNDMzNTMyMzk=","MTE1NDQ5OTUwMDAwMDAwNDI2MDM0Mjc=","MTE1NDAxNzgwMDAwMDAwNDM3MzAxMTc=",]
# DREAM_FACTORY_SHARE_CODES 惊喜工厂 
DREAM_FACTORY_SHARE_CODES = ["20N3vpb8SJ8IhP9KM6hbjA==","HJYZUd7F4k9UBbmhECgjQw==","FIZRGWBsoKZ1KbIkVqob7w==", "ms7qpHyK_Wf4WmI3Cv4JxQ==", "wmXYQAQYpltWuFWEaiIX-g=="]

# JXNC_SHARECODES 京喜农场
JXNC_SHARECODES = ["da605ee5b49922f4d4712a4a8cba3c81", "7b448651deaa6961acef14df1a1992f0", "8083811242d4af8c2e372428305d20ec", "3802dd1c5530d56f725eaf52ad7b144b", "9f971f89687ff726c38f45048397b850","6ea805f5f2aaaf44f794003f5c6ca28a"]

# BOOKSHOP_SHARECODES 京东书店互助码
BOOKSHOP_SHARECODES = ["8eb53dac38ed40e19e774f4b645d85dc","2459a795aa10401ca275ba63850149d9", "47f0f1b272ba49cd8d4a94cc7fcd5402", "56a1062272b4436c874642d5848bb83c","f301d6af98044b97973a80bc0e28f793"]#, "e291f37b47ef44dba9e89dbcf612110c"]
# JD_CASH_SHARECODES 签到现金
JD_CASH_SHARECODES = ["eU9Ya-7mb651823UznQRhA", "eU9YMq7aNa5yrBiBoyVM","Ihg-bOWxYvUj9Gm6iw", "ZE9wPprjEKNehCamshE", "cEPi7ERl_XU"]
# JDNIAN_SHARECODES 京东年兽
JDNIAN_SHARECODES = ["cgxZdTXtI7iO41yaCgao6iJBs_iY8GzLPSF33Ak8VvvDtaHzV8ARHt9AL6U","cgxZdTXteviyuVydVXP9h_LWwhZn4nqryKYaJsBUaAM3di2m7FtItbY","cgxZLmKLJLPZ7gfMDQLGr3TW0we1LXD5EIMWlBWTU6qalOoo0g","cgxZaDXFdsyLnFGxfU3alsEEPaSG-1AukgU9SvlKbNORJh_9ye6G","cgxZfDlXpBINcYeFRGauvnSdL5P1obMGuA"]
# JD_NH 京东年货
JD_NH = ["76334f8e9ecb4a1cabafaf75a096e838","18205e114ce94bfd811122f89131df96","3b8618b10a0d4f6380b53b8dc69e09ef","8a1193d8419c41d59a28a472f8480e99","fedec8a64af04bd0b1ecec129dbd78a3"]





#FruitShareCodes 东东农场
others_fruit = ["8d119151550346cc9bd7f5ac01542c9d","79b3e2056cde4dde88e408d344e6f631", "433982da4897423a878cfc8b9d7ecb72",]
# PLANT_BEAN_SHARECODES 种豆得豆
others_bean = ["ul4b2ndodmxbrozewismvsh37y","5pmuu6qye4rvnr355pppnpgvym","i2m6th3b2gyzdyq2d2em5mth3i", "emhxfc7hmmayfzum4xw54tnwe43h7wlwy7o5jii", ]
# DDFACTORY_SHARECODES 东东工厂 
others_dd_factory = ["T010_bgtRR4b8ACjVWnYaS5kRrbA","T014aV3wl76a_VPeJgCjVWnYaS5kRrbA","T0105bovQx4Y_QCjVWnYaS5kRrbA","T018v_51SRwb8FHWIR2b1ACjVWnYaS5kRrbA",]
# JDZZ_SHARECODES 京东赚赚
others_jd_zz = ["S_bgtRR4b8A","SaV3wl76a_VPeJg","S5bovQx4Y_Q","Sv_51SRwb8FHWIR2b1A"]
# JDJOY_SHARECODES  疯狂joy
others_jd_joy = ["aZSrvYZ2cIY=","JLIkMe0357niDFQafZkDnQ==","AtgLomFU0QM=","qgQxzDdXIFD8c1oz4etGTA=="]
# PETSHARECODES 东东萌宠
others_pet = ["MTAxODc2NTEzMjAwMDAwMDAzMzAyMTI5OQ==","MTAxODc2NTEzNTAwMDAwMDAzMzE4NjMyMw==","MTE1NDQ5OTUwMDAwMDAwNDMyMjIwMjE="]
# DREAM_FACTORY_SHARE_CODES 惊喜工厂 
others_dr_factory = ["7x5NZNPS_tbCTI6W3O9vVQ==","HQL8ZTIJN0nezm_zvcsROA==","_uIsulGorSqHxB-sQqSaiA==","ganFL7VUohd67CfSO7nItA==",]
others_jx_fruit = ["ac0849bec91ac2271079b3a80d420ef7"]
others_jd_book = []
others_jd_cash = []
others_jd_nian = []
others_jd_nh = []


    
def gen_help(name, want,others):
    print(name)
    split_code = "&"
    length = len(want)
    result = []
    result.append(split_code.join(want))
    want.extend(others)
    for i in range(length):
        result.insert(0,split_code.join(want))
    for i in result:
        print(i)
    print("-------------------------------------------------")
        


def gen_all():
    gen_help("FruitShareCodes", FruitShareCodes, others_fruit)  
    gen_help("PLANT_BEAN_SHARECODES", PLANT_BEAN_SHARECODES, others_bean) 
    gen_help("DDFACTORY_SHARECODES",DDFACTORY_SHARECODES, others_dd_factory)
    gen_help("JDZZ_SHARECODES",JDZZ_SHARECODES,others_jd_zz)
    gen_help("JDJOY_SHARECODES",JDJOY_SHARECODES,others_jd_joy)
    gen_help("PETSHARECODES",PETSHARECODES,others_pet)
    gen_help("DREAM_FACTORY_SHARE_CODES",DREAM_FACTORY_SHARE_CODES,others_dr_factory)
    gen_help("JXNC_SHARECODES", JXNC_SHARECODES, others_jx_fruit)
    gen_help("BOOKSHOP_SHARECODES", BOOKSHOP_SHARECODES, others_jd_book)
    gen_help("JD_CASH_SHARECODES", JD_CASH_SHARECODES, others_jd_cash)
    gen_help("JDNIAN_SHARECODES", JDNIAN_SHARECODES, others_jd_nian)
    gen_help("JD_NH",JD_NH,others_jd_nh)


if __name__ == '__main__':
    gen_all()
    