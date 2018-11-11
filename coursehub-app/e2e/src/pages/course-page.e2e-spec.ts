import { CourseCard } from '../components/course-card.co';
import { Search } from '../components/search.co';
import { TestUtils } from '../utils/test-utils.uo';

describe('Test course page', () => {
  let courseCard: CourseCard;
  let search: Search;
  let testUtils: TestUtils;

  beforeEach(() => {
    courseCard = new CourseCard();
    search = new Search();
    testUtils = new TestUtils();
  });

  it('should search for csc165 clicking it should lead to course page', () => {
    testUtils.navigateTo();
    search.getSearchBarInput().click();
    search.typeInSearchBar("CSC165");
    courseCard.getCourseCardHeader().click();
    expect(testUtils.getCurrentPageUrl()).toEqual("http://localhost:4200/course/20043");
  });

  it('should search for csc165 clicking it should lead to course page with populated course card', () => {
    testUtils.navigateTo();
    search.getSearchBarInput().click();
    search.typeInSearchBar("CSC165");
    courseCard.getCourseCardHeader().click();
    expect(testUtils.getCurrentPageUrl()).toEqual("http://localhost:4200/course/20043");
    expect(courseCard.getCourseCardHeader()).toBeDefined();
    expect(courseCard.getCourseCardHeaderText()).toEqual("CSC165H1");
    expect(courseCard.getCourseCardDescriptionText()).toContain("Introduction to abstraction and rigour. Informal");
  });


  it('should populate course card when the course age is loaded directly via perma link', () => {
    testUtils.navigateTo("http://localhost:4200/course/20043");
    expect(courseCard.getCourseCardHeader()).toBeDefined();
    expect(courseCard.getCourseCardHeaderText()).toEqual("CSC165H1");
    expect(courseCard.getCourseCardDescriptionText()).toContain("Introduction to abstraction and rigour. Informal");
  });

});
