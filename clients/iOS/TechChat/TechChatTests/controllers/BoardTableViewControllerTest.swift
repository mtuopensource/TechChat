//
//  BoardTableViewController.swift
//  TechChatTests
//
//  Created by Ryan Philipps on 12/26/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import XCTest
@testable import TechChat

class BoardTableViewControllerTest: XCTestCase {
    private let refresh = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0NTYwMDQ0OSwianRpIjoiODhhZGUzZjljZDFjNGZmYmI5ZjQ1MGNmNzJmODY5OGEiLCJ1c2VyX2lkIjoyfQ.3zYmX9OgqVQdxbLl3lcrkrZk1YMQ3X_Ics_DNLnxKno"
    
    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testBoardRetrieval() {
        User.instance.refreshToken = refresh
        User.instance.refreshAccessIfNeeded(completion: { success in
            if !success {
                XCTFail("The access token was not refresh correctly")
            }
            debugPrint("Access Token: \(String(describing: User.instance.accessToken))")
            let viewController = BoardTableViewController()
            viewController.viewDidLoad()
            let boardsRetrieved = viewController.tableView(viewController.tableView, numberOfRowsInSection: 0)
            XCTAssertGreaterThan(boardsRetrieved, 0)
        })
    }

}
