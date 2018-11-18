//
//  Urls.swift
//  TechChat
//
//  Created by Ryan Philipps on 11/17/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import UIKit

class ApiUrls {
    private static let BaseUrl: String = "https://open-source-at-mtu-tech-chat.herokuapp.com"
    
    enum Urls: String {
        case Login = "/api/token/"
        
        func url() -> URL {
            return URL(string: BaseUrl + self.rawValue)!
        }
    }
}
