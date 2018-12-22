//
//  BoardTableViewCell.swift
//  TechChat
//
//  Created by Ryan Philipps on 11/27/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import UIKit

class BoardTableViewCell: UITableViewCell {
   
    
    @IBOutlet weak var titleLabel: UILabel!
    @IBOutlet weak var descriptionLabel: UILabel!
    

    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}
