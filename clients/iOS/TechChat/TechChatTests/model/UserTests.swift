//
//  UserTests.swift
//  TechChatTests
//
//  Created by Ryan Philipps on 12/22/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import XCTest

class UserTests: XCTestCase {
    private let refresh = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0NTYwMDQ0OSwianRpIjoiODhhZGUzZjljZDFjNGZmYmI5ZjQ1MGNmNzJmODY5OGEiLCJ1c2VyX2lkIjoyfQ.3zYmX9OgqVQdxbLl3lcrkrZk1YMQ3X_Ics_DNLnxKno"
    
    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    func testCreationFromJSON() {
        let json = ["refresh": "this is a refresh token", "access": "this is an access token"]
        let userCreated = User.instance.setData(json: json)
        assert(userCreated, "The user was not created with the json input")
        assert(User.instance.accessToken == json["access"])
        assert(User.instance.refreshToken == json["refresh"])
    }
    
    func testGoodAccessRefresh() {
        User.instance.refreshToken = self.refresh
        User.instance.refreshAccessIfNeeded(completion: { success in
            assert(success)
            assert(User.instance.accessToken != nil)
        })
    }
    


}
