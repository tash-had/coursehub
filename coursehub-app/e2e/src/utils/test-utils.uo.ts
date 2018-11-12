import { browser, by, element } from 'protractor';

export class TestUtils {
    navigateTo(link="/") {
        return browser.get(link);
    }

    getCurrentPageUrl() {
        return browser.getCurrentUrl();
    }

    navigateBack() {
        browser.navigate().back();
    }
    
    log(msg: any){
        browser.executeScript("console.log('" + msg + "');");
        browser.sleep(100000);
    }
}