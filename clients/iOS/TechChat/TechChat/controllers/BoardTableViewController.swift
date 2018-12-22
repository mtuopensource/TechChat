//
//  BoardTableViewController.swift
//  TechChat
//
//  Created by Ryan Philipps on 11/27/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import UIKit
import Alamofire

class BoardTableViewController: UITableViewController {

   var boards = [Board]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        
        if boards.count == 0 {
            self.retreiveBoards() { success in
                if success {
                    self.tableView.reloadData()
                }
            }
        }
        
        
        

        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem
    }

    // MARK: - Table view data source

    override func numberOfSections(in tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        return 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        return boards.count
    }

    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cellIdentifier = "BoardCell"
        
        guard let cell = tableView.dequeueReusableCell(withIdentifier: cellIdentifier, for: indexPath) as? BoardTableViewCell else {
            fatalError("This cell should have been a board table cell")
        }
        
        let board = boards[indexPath.row]
        cell.titleLabel.text = board.title
        cell.descriptionLabel.text = board.description
        
        
        return cell
        
        
    }
    

    /*
    // Override to support conditional editing of the table view.
    override func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCellEditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            // Delete the row from the data source
            tableView.deleteRows(at: [indexPath], with: .fade)
        } else if editingStyle == .insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(_ tableView: UITableView, moveRowAt fromIndexPath: IndexPath, to: IndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(_ tableView: UITableView, canMoveRowAt indexPath: IndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */
    
    typealias GetBoardCompletion = (Bool) -> ()
    private func retreiveBoards(completion: @escaping GetBoardCompletion) {
        // set up the request
        let boardURL = ApiUrls.Urls.Boards.url()
        let token = User.instance.accessToken!
        let headers = ["Authorization": "Bearer \(token)"]
        
        Alamofire.request(boardURL, headers: headers).validate()
        .responseJSON(completionHandler: { response in
            debugPrint("request: \(response.request!)")
            debugPrint("response: \(response)")
            switch response.result {
                
            case .success:
                var newBoards = [Board]()
                // take the json and turn it into some board objects
                if let json = response.result.value as? [[String: Any]] {
                    json.forEach({ boardJson in
                        let id = boardJson["id"] as! Int
                        let title = boardJson["title"] as! String
                        let description = boardJson["description"] as! String
                        let board = Board(id: id, title: title, description: description)
                        newBoards += [board]
                    })
                    self.boards += newBoards
                    completion(true)
                    return
                }
                completion(false)
                return
                
            case .failure(let error):
                debugPrint(error)
                completion(false)
                return
            }
            
        })
       
    }

}
