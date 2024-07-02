import requests
from requests import Response
from pydantic import BaseModel, RootModel, Field, field_validator,ConfigDict

def __download_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    try:
        res:Response = requests.get(url)
    except Exception:
        raise Exception("連線失敗")
    else:
        all_data:dict[any] = res.json()
        return all_data
    

class Info(BaseModel):
    sna:str
    sarea:str
    mday:str
    ar:str
    act:str
    updateTime:str
    total:int
    rent_bikes:int = Field(alias="available_rent_bikes")
    lat:float = Field(alias="latitude")
    lng:float = Field(alias="longitude")
    retuen_bikes:int = Field(alias="available_return_bikes")
    
    model_config = ConfigDict(          #用來讓兩個名稱都能通用，不用一項一項改
        populate_by_name=True,
    )
    
    @field_validator('sna',mode='before')
    @classmethod
    def flex_string(cls,value:str)->str:
        return value.split(sep="_")[-1]

class Youbike_Data(RootModel):
    root:list[Info]

def load_data()->list[dict]:
    try:
        all_data:dict[any] = __download_json()
    except Exception as error:
        print(error)
        
    youbike_data:Youbike_Data = Youbike_Data.model_validate(all_data)
    data = youbike_data.model_dump()
    return data
    


class FilterData(object):   #建立一個用來包含method的class，被稱為StaticMethod，object只是不用繼承時寫的
    @staticmethod
    def get_selected_site(sna:str,data:list[dict]) -> Info:
        '''
        def abc(item:dict) -> bool:              #建立一個僅用於此function的function
            if item['sna'] == sna:              #從data中輸入資料，其中key值為'sna'的欄位，若內容等於使用get_selected_site時輸入的sna時
                return True
            else:
                return False
        right_list:list[dict]=list(filter(abc,data))          #filter為用前面的公式來處理後面的資料，回傳出來類型為filter，要再用list轉換
        用lambda修改成以下一行
        '''
        #lambda用法是 True if xxxx else false
        right_list:list[dict]=list(filter(lambda item:True if item['sna']==sna else False,data))
        # return right_list[0]['lat'],right_list[0]['lng']    #為什麼是0
        data:dict = right_list[0]
        return Info.model_validate(data)
        