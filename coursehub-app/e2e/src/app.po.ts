import { browser, by, element } from 'protractor';

export class AppPage {
  navigateTo(link="/") {
    return browser.get(link);
  }

  getCurrentPageUrl() {
    return browser.getCurrentUrl();
  }

  getSearchBarInput() {

    return element(by.css('app-searchbar input'));
  }

  getCourseCardHeader() {
    return element(by.css('#courseCardHeader'));
  }

  getCourseCardHeaderText() {
    return element(by.css('#courseCardHeader h2')).getText();
  }

  getCourseCardDescriptionText() {
    return element(by.css('.readMoreCurrentText')).getText();
  }

  typeInSearchBar(text: string) {
    browser.actions().sendKeys(text).perform();
  }

  log(msg: any){
    browser.executeScript("console.log('" + msg + "');");
    browser.sleep(100000);
  }
}
