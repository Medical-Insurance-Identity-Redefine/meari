//
//  InputViewController.swift
//  uploadImage
//
//  Created by JUEUN KIM on 2021/08/24.
//

import UIKit

class InputViewController: UIViewController, UITextFieldDelegate {
    @IBOutlet var idNumberView: UIView!
    @IBOutlet var hospReasonView: UIView!
    @IBOutlet var inputTextfield: UITextField!
    @IBOutlet var emergency: UIView!
    
    let diseaseCode = ""
    override func viewDidLoad() {
        super.viewDidLoad()
        self.idNumberView.layer.cornerRadius = 15
        self.idNumberView.clipsToBounds = true
        self.hospReasonView.layer.cornerRadius = 15
        self.hospReasonView.clipsToBounds = true
        
        self.emergency.layer.cornerRadius = 15
        self.emergency.clipsToBounds = true
        
        
        inputTextfield.delegate = self
        // Do any additional setup after loading the view.
        inputTextfield.text = diseaseCode
    }
    func onThridVCAction(data : String)
       {
           self.inputTextfield.text = data
       }
    
    @objc func textFieldShouldReturn(_ textField: UITextField) -> Bool {
            self.view.endEditing(true)
        let vcName = self.storyboard?.instantiateViewController(withIdentifier: "searchTableView")
        vcName?.modalTransitionStyle = .coverVertical
        self.present(vcName!, animated: true, completion: nil)
            return false
    }

}

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */
