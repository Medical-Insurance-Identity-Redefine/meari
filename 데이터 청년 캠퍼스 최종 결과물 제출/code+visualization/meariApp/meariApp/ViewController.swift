//
//  ViewController.swift
//  UploadPhoto
//
//  Created by Mahvish Syed on 25/04/21.
//  Copyright © 2021 Mahvish Syed. All rights reserved.
//

import UIKit
//import Alamofire
//import Kingfisher


class ViewController: ExtensionVC, UIImagePickerControllerDelegate & UINavigationControllerDelegate {

    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet var submitButton: UIButton!
    @IBOutlet var bigView: UIView!
    @IBOutlet var uploadButton: UIButton!
    
    var imageViewController = UIImagePickerController()
    
    override func viewDidLoad() {
        self.view.backgroundColor = .white
        super.viewDidLoad()
        imageViewController.delegate = self
        self.submitButton.isHidden = true
        self.bigView.layer.cornerRadius = 15
        self.bigView.clipsToBounds = true
        self.submitButton.layer.cornerRadius = 10
        self.submitButton.clipsToBounds = true
        self.uploadButton.layer.cornerRadius = 10
        self.uploadButton.clipsToBounds = true
        

        print("viewload됐다잉~")
    }

    @IBAction func selectImage(_ sender: UIButton) {
        imageViewController.sourceType = .photoLibrary
        imageViewController.allowsEditing = true
        present(imageViewController, animated: true, completion: nil)
    }
        func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
            if let pickedImage = info[.originalImage] as? UIImage {
                    imageView.contentMode = .scaleAspectFit
                    imageView.image = pickedImage
            }
            dismiss(animated: true, completion: nil)
            var sv = UIView()
            sv = UIViewController.displaySpinner(onView: self.view)
            DispatchQueue.main.asyncAfter(deadline: .now() + 3.0) {
                UIViewController.removeSpinner(spinner: sv)
                let alert = UIAlertController(title: "비급여 진료비 확인 서비스 대상입니다.", message: """
                    92%의 확률로 환불이 가능한 항목입니다.
                    해당 서비스를 신청하시려면 서류제출하기 버튼을 눌러주세요.
                    """, preferredStyle: .alert)
                let defaultAction = UIAlertAction(title: "OK", style: .destructive, handler : nil)
                alert.addAction(defaultAction)
                self.present(alert, animated: true, completion: nil)
            }
            self.submitButton.isHidden = false
        }
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?){

          self.view.endEditing(true)

    }
        
    @IBAction func submitButtonTouchInside(_ sender: Any) {
        let alert = UIAlertController(title: "신청완료", message: "", preferredStyle: .alert)
        let defaultAction = UIAlertAction(title: "OK", style: .destructive, handler : nil)
        alert.addAction(defaultAction)
        present(alert, animated: false, completion: nil)
    }
}

//
//class ViewController: UIViewController, , UINavigationControllerDelegate,UITextFieldDelegate {
//
//
//    @IBOutlet var imageView : UIImageView!
//    var imagePicker = UIImagePickerController()
//    @IBAction func touchUpUploadButton(_ sender: UIButton) {
//
//        //이미지뷰의 이미지 가져오기
//        guard let image: UIImage = self.imageView.image else {
//            return
//        }
//        //image를 전달할 수 있는 데이타로 변환
//        guard let imageData : Data = image.jpegData(compressionQuality: 0.5) else {
//            return
//        }
//
//        AF.upload(multipartFormData: {
//            (multipartFormData)  in
//            multipartFormData.append(imageData, withName : "image",fileName: "image.jpeg", mimeType:"image/jpeg")
//
//
//        }, to: "http://clubneverest.c1.biz/photo", encodingCompletion: { encodingResult in
//            switch encodingResult {
//            case .success(let upload, _, _):
//                upload.responseJSON { response in
//                    debugPrint(response)
//
//                    let presentAlert : UIAlertController = UIAlertController(title: "작성꿀", message: "작성되었습니다.", preferredStyle : UIAlertController.Style.alert)
//
//                    let successAction : UIAlertAction = UIAlertAction(title: "확인", style: UIAlertAction.Style.cancel) { (action: UIAlertAction) in
//                        //확인버튼을 누르면 실행될 코드
//
//                        self.navigationController?.popViewController(animated: true)
//
//                    }
//                    presentAlert.addAction(successAction)
//
//
//
//                    self.present(presentAlert, animated: true, completion: nil)
//
//                }
//
//            case .failure(let encodingError) :
//                print(encodingError)
//            }
//        })
//    }
//
//    override func viewDidLoad() {
//        self.imageView.isUserInteractionEnabled = true
//        self.imageView.addGestureRecognizer(UITapGestureRecognizer(target: self, action: #selector(CreateViewController.getGallery(sender:))))
//    }
//
//    @objc func getGallery(sender:UITapGestureRecognizer) {
//        if(sender.state == .ended) {
//            if UIImagePickerController.isSourceTypeAvailable(.photoLibrary) {
//                print("a")
//                imagePicker.delegate = self
//                imagePicker.sourceType = .photoLibrary
//                imagePicker.allowsEditing = false
//                self.present(imagePicker, animated: true, completion: nil)
//            }
//        }
//    }
//

//
//
//
//
//}
//
