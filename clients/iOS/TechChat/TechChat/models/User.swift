//
//  User.swift
//  TechChat
//
//  Created by Ryan Philipps on 11/17/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import Foundation
import Alamofire

final class User {
    private let LIFE_TIME = 20.0 // in miliseconds
    
    var refreshToken: String
    var accessToken: String?
    private var tokenLifeTime: Double
    
    static let instance = User()
    
    private init() {
        self.refreshToken = ""
        tokenLifeTime = -1
    }
    
    func setData(json: [String: Any]) -> Bool {
        guard let refreshToken = json["refresh"] as? String,
        let accessToken = json["access"] as? String else {
            return false
        }
        
        self.accessToken = accessToken
        self.refreshToken = refreshToken
        self.tokenLifeTime = Date().timeIntervalSince1970
        return true
    }
    // a function that takes in a boolean saying wether the token is good or not
    typealias RefreshCompletion = (Bool) -> ()
    public func refreshAccessIfNeeded(completion: @escaping RefreshCompletion) {
        if accessTokenNeedsRefresh() {
            let refreshURL = ApiUrls.Urls.Refresh.url()
            Alamofire.request(refreshURL, parameters: ["refresh": User.instance.refreshToken], encoding: URLEncoding.default)
            .validate().responseJSON(completionHandler: { response in
                debugPrint("request: \(response.request!)")
                debugPrint("response: \(response)")
                debugPrint("error: \(String(describing: response.error))")
                if let json = response.result.value as? [String: Any] {
                    self.accessToken = json["access"] as? String
                    self.tokenLifeTime = Date().timeIntervalSince1970
                    completion(true)
                    return 
                }
                else {
                    completion(false)
                    return
                }
            })
        }
        completion(true)
        return
    }
    
    func accessTokenNeedsRefresh() -> Bool {
        let today = Date().timeIntervalSince1970
        return (today - tokenLifeTime) > (LIFE_TIME)
    }
    
    
    
    
    
}


