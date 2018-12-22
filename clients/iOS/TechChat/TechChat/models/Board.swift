//
//  Board.swift
//  TechChat
//
//  Created by Ryan Philipps on 11/27/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import Foundation


class Board {
    var title: String
    var description: String
    var id: Int
    
    init(id: Int, title:String, description:String) {
        self.id = id
        self.title = title
        self.description = description
    }
}
