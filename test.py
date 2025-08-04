from api_manager import search_api_key
from api_manager import store_api_key
import time

def main():
    if a:= search_api_key("TeST") == "this is a test file for api_manager".strip():
        print("search existing api file , test passed ,done")
        print(a)
        print(search_api_key("TeST").strip())
    else:
        print("failed search api file test")

    time.sleep(1)

    names = {
        "any_test":"gGGT^T^kkru7489473993003 ",
        "     ":"DDD",
        "dddd":"     ",
        "test": "dddfdssddc",
        "no_file" : "hffjf",
        "nvvnfj": "no_key"

    }

    res = ["file any_test created , and api key saved","file cannot be created","file already exist, cannot be created again"]
    tests = ["normal test","blank name test","blank api key test","existing file test", "'no_file' test","'no_key' test"]
    for name,key ,test in zip(names.keys(),names.values(),tests):
        a = store_api_key(name,key)
        
        if a in res:
            print(f"test passed, {test} ")
            if name == "any_test" :
                b=search_api_key(name)
                if b == "gGGT^T^kkru7489473993003":
                    print("valu check also passed, of newly created file")
                else:
                    print("value check failed , of newly created file")
        else:
            print("test failed or check res list "+test)
        
if __name__ == "__main__":
    main()