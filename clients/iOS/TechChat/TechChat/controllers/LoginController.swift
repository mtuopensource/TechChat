//
//  LoginController.swift
//  TechChat
//
//  Created by Ryan Philipps on 11/15/18.
//  Copyright © 2018 OpenSourceClub. All rights reserved.
//

import UIKit
import Alamofire


class LoginController: UIViewController {

    @IBOutlet weak var emailInput: UITextField!
    @IBOutlet weak var passwordInput: UITextField!
    
    // sets the status bar to be a light color
    override var preferredStatusBarStyle: UIStatusBarStyle {
        return .lightContent
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // change the status bar color
        setNeedsStatusBarAppearanceUpdate()
       
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    
    
    
    @IBAction func attemptLogin(_ sender: UIButton) {
        guard let email = emailInput.text, !email.isEmpty else {
            return
        }
        guard let password = passwordInput.text, !password.isEmpty else {
            return // send an error message or something
        }
        let authParms = ["username": email, "password": password]
        let loginUrl = ApiUrls.Urls.Login.url()
        
        Alamofire.request(loginUrl, method: .post, parameters: authParms, encoding: URLEncoding.default)
            .validate()
            .responseJSON(completionHandler: {  response in
                debugPrint("request: \(response.request)")
                debugPrint("response: \(response)")
                debugPrint("Error: \(response.error)")
            
                
                
                if let json = response.result.value as? [String: Any] {
                    let refreshToken = json["refresh"]
                    let accessToken = json["access"]
                    self.performSegue(withIdentifier: "login", sender: nil)
                }
        })
       
    }
    
    
    
}

