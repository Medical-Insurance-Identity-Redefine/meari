//
//  lastViewController.swift
//  uploadImage
//
//  Created by JUEUN KIM on 2021/08/22.
//

import UIKit

class lastViewController: UIViewController {

    @IBOutlet var bigView: UIView!
    @IBOutlet var progressView: UIView!
    @IBOutlet var resultView: UIView!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        self.bigView.layer.cornerRadius = 15
        self.bigView.clipsToBounds = true
        self.progressView.layer.cornerRadius = 15
        self.progressView.clipsToBounds = true
        self.resultView.layer.cornerRadius = 15
        self.resultView.clipsToBounds = true
        // Do any additional setup after loading the view.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
