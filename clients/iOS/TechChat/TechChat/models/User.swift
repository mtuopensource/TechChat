//
//  User.swift
//  TechChat
//
//  Created by Ryan Philipps on 11/17/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import Foundation

final class User {
    private let LIFE_TIME = 20.0 // in miliseconds
    
    var refreshToken: String
    var accessToken: String?
    var tokenLifeTime: Double
    
    static let instance = User()
    
    private init() {
        self.refreshToken = ""
        tokenLifeTime = -1
    }
    
    func setData(with json: [String: Any]) -> Bool {
        guard let refreshToken = json["refresh"] as? String,
        let accessToken = json["access"] as? String else {
            return false
        }
        
        self.accessToken = accessToken
        self.refreshToken = refreshToken
        self.tokenLifeTime = Date().timeIntervalSince1970
        return true
    }
    
    
    public func refreshAccessIfNeeded() {
        
    }
    
    private func accessTokenNeedsRefresh() -> Bool {
        let today = Date().timeIntervalSince1970
        return (today - tokenLifeTime) > (LIFE_TIME)
    }
    
    
    
    
    
}


