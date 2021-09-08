//
//  SearchViewController.swift
//  meariApp
//
//  Created by JUEUN KIM on 2021/08/27.
//

import UIKit

class SearchViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    struct diseaseModel {
        var code : String
        var diseaseName : String
    }
    
    var diseaseList = [diseaseModel(code: "K291", diseaseName: "급성위염"),
                   diseaseModel(code: "K292", diseaseName: "알코올성 위염"),
                   diseaseModel(code: "K295", diseaseName: "상세불명의 만성위염")]

    @IBOutlet var tableView: UITableView!
//    @IBOutlet var searchButton: UIButton!
    override func viewDidLoad() {
        super.viewDidLoad()
//        self.tableView.isHidden = true
        self.tableView.delegate = self
        self.tableView.dataSource = self
        self.tableView.register(UITableViewCell.self, forCellReuseIdentifier: "TableViewCell")
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return diseaseList.count
    }

    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
            let cell: UITableViewCell = tableView.dequeueReusableCell(withIdentifier: "TableViewCell", for: indexPath) as UITableViewCell
        cell.textLabel?.font = UIFont(name: "KoreanPGDM", size: 18)
        cell.textLabel?.textColor = .darkText
        cell.backgroundColor = UIColor(red: 223, green: 201, blue: 131, alpha: 1.0)
        if indexPath.row == 0{
            cell.textLabel?.text = "급성위염"
        }else if indexPath.row == 1{
            cell.textLabel?.text = "알코올성 위염"
        }else {
            cell.textLabel?.text = "상세불명의 만성위염"
        }
            return cell
        }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        dismiss(animated: true, completion: nil)
    }
    
}
