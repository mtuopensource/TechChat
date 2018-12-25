//
//  LoginUITests.swift
//  TechChatUITests
//
//  Created by Ryan Philipps on 12/24/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import XCTest
@testable import TechChat

class LoginUITests: XCTestCase {

    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.

        // In UI tests it is usually best to stop immediately when a failure occurs.
        continueAfterFailure = false

        // UI tests must launch the application that they test. Doing this in setup will make sure it happens for each test method.
        XCUIApplication().launch()

        // In UI tests it’s important to set the initial state - such as interface orientation - required for your tests before they run. The setUp method is a good place to do this.
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }
    
    private func enterCredentials(email: String, password: String) {
        let app = XCUIApplication()
        let emailInput = app.textFields["Email"]
        emailInput.tap()
        emailInput.typeText(email)
        let passwordSecureTextField = app.secureTextFields["password"]
        passwordSecureTextField.tap()
        passwordSecureTextField.typeText(password)
        app.buttons["Login"].tap()
    }

    /**
     * This test enters in the test user credentials
     * then it will check if the board table is viewable to the user
     */
    func testGoodCredentials() {
        let app = XCUIApplication()
        enterCredentials(email: "test@mtu.edu", password: "test")
        let boardTable = app.tables["BoardTable"]
        let predicate = NSPredicate(format: "hittable == true")
        let expectation = XCTNSPredicateExpectation(predicate: predicate, object: boardTable)
        
        let result = XCTWaiter().wait(for: [expectation], timeout: 5)
        XCTAssertTrue(result == .completed)
        
    
    }
    

}
