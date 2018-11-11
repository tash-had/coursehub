import { browser, by, element } from 'protractor';

export class Search {
    getSearchBarInput() {
        return element(by.css('app-searchbar input'));
    }

    getSearchBarInputValue() {
        return element(by.css('app-searchbar input')).getAttribute("value");
    }

    typeInSearchBar(text: string) {
        browser.actions().sendKeys(text).perform();
    }
}