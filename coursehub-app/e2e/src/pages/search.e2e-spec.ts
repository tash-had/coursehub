import { Search } from '../components/search.co';
import { CourseCard } from '../components/course-card.co';
import { TestUtils } from '../utils/test-utils.uo'

describe('Test course search', () => {
  let courseCard: CourseCard;
  let search: Search;
  let testUtils: TestUtils;

  beforeEach(() => {
    courseCard = new CourseCard();
    search = new Search();
    testUtils = new TestUtils();
  });

  it('should search for csc165 and have one search result', () => {
    search.navigateTo();
    search.getSearchBarInput().click();
    search.typeInSearchBar("CSC165");

    expect(courseCard.getCourseCardHeader()).toBeDefined();
    expect(courseCard.getCourseCardHeaderText()).toEqual("CSC165H1");
    expect(courseCard.getCourseCardDescriptionText()).toEqual("Introduction to abstraction and rigour. Informal introduction to logical notation and reasoning. Understanding, using and developing precise expressio...");
  });

  it('should search for csc165 and go to corresponding course page', () => {
    search.navigateTo();
    search.getSearchBarInput().click();
    search.typeInSearchBar("CSC165");

    expect(courseCard.getCourseCardHeader()).toBeDefined();
    expect(courseCard.getCourseCardHeaderText()).toEqual("CSC165H1");

    courseCard.getCourseCardHeader().click();
    
  });
});