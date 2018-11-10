import { browser, by, element } from 'protractor';

export class CourseCard {  
  getCourseCardHeader() {
    return element(by.css('#courseCardHeader'));
    }

    getCourseCardHeaderText() {
    return element(by.css('#courseCardHeader h2')).getText();
    }

    getCourseCardDescriptionText() {
    return element(by.css('.readMoreCurrentText')).getText();
    }
}

// FIX TESTS