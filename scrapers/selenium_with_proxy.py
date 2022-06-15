import os
import zipfile
import hashlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

proxy = "102.165.1.59:5432"
credentials = "gpfc8:usas32wk"

dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, "chromedriver", "chromedriver_v102.exe")

path_to_chrome_binary = "C:\Program Files\Google\Chrome\Application\chrome.exe"
path_to_chromedriver_binary = webdriver.Chrome(path)


def generate_extension(proxy, credentials):
    ip, port = proxy.split(":")
    login, password = credentials.split(":")
    manifest_json = """
  {
      "version": "1.0.0",
      "manifest_version": 2,
      "name": "Chrome Proxy",
      "permissions": [
          "proxy",
          "tabs",
          "unlimitedStorage",
          "storage",
          "",
          "webRequest",
          "webRequestBlocking"
      ],
      "background": {
          "scripts": ["background.js"]
      },
      "minimum_chrome_version":"22.0.0"
  }
  """

    background_js = """
  var config = {
          mode: "fixed_servers",
          rules: {
          singleProxy: {
              scheme: "http",
              host: "%s",
              port: parseInt(%s)
          },
          bypassList: ["localhost"]
          }
      };

  chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

  function callbackFn(details) {
      return {
          authCredentials: {
              username: "%s",
              password: "%s"
          }
      };
  }

  chrome.webRequest.onAuthRequired.addListener(
              callbackFn,
              {urls: [""]},
              ['blocking']
  );
  """ % (
        ip,
        port,
        login,
        password,
    )

    sha1 = hashlib.sha1()
    sha1.update(("%s:%s" % (proxy, credentials)).encode("utf-8"))
    filename = sha1.hexdigest() + ".zip"

    with zipfile.ZipFile(filename, "w") as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return filename


extension_name = generate_extension(proxy, credentials)
options = Options()
options.binary_location = path_to_chrome_binary
options.add_extension(extension_name)
driver = webdriver.Chrome(
    executable_path=path_to_chromedriver_binary,
    options=options,
)
driver.get("http://api.privateproxy.me:10738/")
element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "pre"))
)
print(element.text)
driver.quit()
os.remove(extension_name)
