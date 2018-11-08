import { AppPage } from './app.po';

describe('Test course search', () => {
  let page: AppPage;

  beforeEach(() => {
    page = new AppPage();
  });

  it('should search for csc165 and have one search result', () => {
    page.navigateTo();
    page.getSearchBarInput().click();
    page.typeInSearchBar("CSC165");

    expect(page.getCourseCardHeader()).toBeDefined();
    expect(page.getCourseCardHeaderText()).toEqual("CSC165H1");
    expect(page.getCourseCardDescriptionText()).toEqual("Introduction to abstraction and rigour. Informal introduction to logical notation and reasoning. Understanding, using and developing precise expressio...");
  });

  it('should search for csc165 clicking it should lead to course page', () => {
    page.navigateTo();
    page.getSearchBarInput().click();
    page.typeInSearchBar("CSC165");
    page.getCourseCardHeader().click();
    expect(page.getCurrentPageUrl()).toEqual("http://localhost:4200/course/20043");
  });

  it('should search for csc165 clicking it should lead to course page with populated course card', () => {
    page.navigateTo();
    page.getSearchBarInput().click();
    page.typeInSearchBar("CSC165");
    page.getCourseCardHeader().click();
    expect(page.getCurrentPageUrl()).toEqual("http://localhost:4200/course/20043");
    expect(page.getCourseCardHeader()).toBeDefined();
    expect(page.getCourseCardHeaderText()).toEqual("CSC165H1");
    expect(page.getCourseCardDescriptionText()).toEqual("Introduction to abstraction and rigour. Informal introduction to logical notation and reasoning. Understanding, using and developing precise expressio...");
  });


  it('should populate course card when the course age is loaded directly via perma link', () => {
    page.navigateTo("http://localhost:4200/course/20043");
    expect(page.getCourseCardHeader()).toBeDefined();
    expect(page.getCourseCardHeaderText()).toEqual("CSC165H1");
    expect(page.getCourseCardDescriptionText()).toEqual("Introduction to abstraction and rigour. Informal introduction to logical notation and reasoning. Understanding, using and developing precise expressio...");
  });
});
