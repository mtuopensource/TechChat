//
//  PostController.swift
//  TechChat
//
//  Created by Ryan Philipps on 3/18/19.
//  Copyright © 2019 OpenSourceClub. All rights reserved.
//

import Foundation
import UIKit



class PostTableViewController : UITableViewController {
    
    var board: Board?
    
    override func viewDidLoad() {
        // code here
        if let board = board {
            navigationItem.title = "Posts for \(board.title)"
        }
        
    }
    
    @IBAction func cancel(_ sender: UIBarButtonItem) {
        
    }
    
    
}
