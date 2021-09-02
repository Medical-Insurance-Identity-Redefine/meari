# MEARI

<img src="https://user-images.githubusercontent.com/87626172/131877946-3ad59fb4-c608-45d7-b744-97f6dd0d85fd.png" width="135" align = "left">

```
🍎 2021 데이터청년캠퍼스 <빅리더 아카데미> 🍎

Big Leader Academy
- 2021. 06. 28 ~ 2021. 08. 30

AI를 활용한 비급여 진료비 자가점검 서비스😊
```


<br/>

## 목차

- [개발환경 및 사용한 라이브러리](#개발환경-및-사용한-라이브러리)

- [서비스 workflow](#서비스-workflow)

- [기능 개발여부/담당자](#기능-개발여부/담당자)

- [핵심기능 구현 방법](#핵심기능-구현-방법)

- [팀원 역할 및 소개](팀원-역할-및-소개)

- [새롭게 알게 된 것](#새롭게-알게-된-것)

### 개발환경 및 사용한 라이브러리
|                       라이브러리                    |               목적                 |      
| :------------------------------------------------: | :------------------------------: |
|                        pandas                      |        데이터 분석 및 전처리      |
|                       lightgbm                     |           머신러닝 모델          |
|                       xgboost                      |           머신러닝 모델          |
|                       catboost                     |           머신러닝 모델          |
|                       sklearn                      |     머신러닝 모델, 성능지표 등    | 
|                       optuna                       |       하이퍼파라미터 최적화       |
|                       pickle                       |   머신러닝 모델 저장 및 불러오기  |
|                 matplotlib, seaborn                |            데이터 시각화         |
|                       Nanonets                     |              OCR API            |
|                 google cloud vision                |              OCR API            |
|                        openCV                      |              영상처리            |
|                      rhinoMorph                    |            형태소분석기          |
<br>

### 서비스 workflow
![image](https://user-images.githubusercontent.com/87626172/131874143-de4d3444-1cca-4d11-9b9a-94a83ba880e0.png)


![KakaoTalk_Photo_2021-01-15-22-54-18](https://user-images.githubusercontent.com/22820675/104735258-bfcb3f80-5784-11eb-99d9-66e6113e972a.png)



### 기능 개발여부/담당자

|    기술     |        기능        | 담당자 | 구현 여부 |
| :---------: | :---------------------: | :----: | :-------: |
|  데이터전처리   |        데이터정제         |  성현  |     ✅     |
|  OpenCV + OCR   |        서류읽어오기         |  주은  |     ✅     |
|   NLP    |         사전제작          |  기표  |     ✅     |
|  Machine Learning   |        예측모델제작        |  규영  |     ✅     |
|      어플제작       |        프로토타입         |  주은  |     ✅     |



### 파트별 중요 코드
1. 데이터전처리

   ~~~python
   // 캘린더 정보 저장을 위한 변수
   var calendarDictionary: [String : [FSCalendarModel]] = [:]
   
   guard let promise: [FSCalendarModel] = calendarDictionary[day] else { return UICollectionViewCell() }
   if promise[indexPath.row].isNotice == 0 {
     let cell: CalendarCollectionViewCell = collectionView.dequeueCell(forIndexPath: indexPath)
   	cell.calendar = promise[indexPath.row]
   	cell.fetchCalendar()
   	cell.fetchCategory()
   	cell.fetchTime()
   	return cell
   } else {
   	let cell: NoticeCollectionViewCell = collectionView.dequeueCell(forIndexPath: indexPath)
   	cell.calendar = promise[indexPath.row]
   	cell.fetchCalendar()
   	cell.fetchTime()
   	return cell
   }
   
   ~~~

2. OpenCV + OCR

   ```swift
   func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
   		let cell: MessageDetailTableViewCell = tableView.dequeueCell(forIndexPath: indexPath)
   		if self.userOrOwner == 0 {
   			if self.status[indexPath.row] == 0 {
   				cell.titleLabel.text = "문의사항이 등록되었어요!"
   				cell.contextLabel.attributedText = self.makeAttributed(
   					context: "아래의 버튼을 눌러\n약속시간을 정해보세요."
   				)
   				cell.transitionButton.addTarget(self,
   																				action: #selector(didTapConfirmButton(_:)),
   																				for: .touchUpInside
   				)
   				cell.transitionButton.setTitle("약속 확정하기", for: .normal)
   			}
   			else if self.status[indexPath.row] == 1 {
   				cell.titleLabel.text = "약속이 확정되었어요!"
   				var confirmedPromise = "\(self.confirmedPromiseOption)예정이에요\n 캘린더에서 일정을 확인해보세요."
   				cell.contextLabel.attributedText = self.makeAttributed(context: confirmedPromise)				
   				cell.transitionButton.addTarget(self,
   																				action: #selector(didTapCalendarButton(_:)),
   																				for: .touchUpInside)
   				cell.transitionButton.setTitle("캘린더 보기", for: .normal)
   			}
   			else if self.status[indexPath.row] == 2 {
   				cell.titleLabel.text = "약속 수정 요청을 보냈어요!"
   				cell.contextLabel.attributedText = self.makeAttributed(
   					context: "앞으로도 하우징과 함께\n자취생과 소통해보세요!"
   				)
   				cell.transitionButton.snp.makeConstraints {
   					$0.height.equalTo(0)
   				}
   			}
   			...
   ```

### 팀원 역할 및 소개

| <IMG src="https://https://github.com/yooseonghyeon.png?size=100" width="150"> | <IMG src="https://github.com/JubyKim.png?size=100" width="150"> | <IMG src="https://github.com/fluffyword.png?size=100" width="150">| <IMG src="https://https://github.com/Giggle1998.png?size=100" width="150"> |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|                            유성현                            |                            김주은                            |                            이규영                            |                            이기표                            |

