//
//  User.swift
//  TechChat
//
//  Created by Ryan Philipps on 11/17/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import Foundation

class User {
    var refreshToken: String
    var accessToken: String?
    
    init(refreshToken: String) {
        self.refreshToken = refreshToken
    }
    
    init?(with json: [String: Any]) {
        guard let refreshToken = json["refresh"] as? String,
        let accessToken = json["access"] as? String else {
            return nil
        }
        
        self.accessToken = accessToken
        self.refreshToken = refreshToken
    }
    
    
}


