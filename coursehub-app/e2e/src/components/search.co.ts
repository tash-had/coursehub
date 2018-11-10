import { browser, by, element } from 'protractor';

export class Search {
    getSearchBarInput() {
        return element(by.css('app-searchbar input'));
    }

    typeInSearchBar(text: string) {
        browser.actions().sendKeys(text).perform();
    }
}