'use strict'
var http = new XMLHttpRequest();

http.open('GET', 'http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=apollo11&facet_field=day_of_week&begin_date=19000101&end_date=20180101&api-key=94a121ba1db24850b47a7d08031bf21a', true);
http.send();

function parser(freshData){
  freshData = JSON.parse(freshData)
  return freshData;
}

function arrangeData(documentObject){
  var articleArray = documentObject.response.docs;
  var allArticles = [];
  for(var i = 0; i < articleArray.length;i++){
    var article = {
      'headline': articleArray[i].headline.main,
      'snippet': articleArray[i].snippet,
      'publication_date': articleArray[i].pub_date,
      'url': articleArray[i].web_url
    }
    allArticles.push(article);
  }
    return allArticles;
  }

  function applyToHtml(objectArray){
    for(var i = 0; i < objectArray.length; i++){
      var containArticles = document.querySelector('.articles');
      var article = document.createElement('div');
      var link = document.createElement('a');
      containArticles.appendChild(article);
      containArticles.appendChild(link);
      article.innerHTML = 'HEADLINE: ' + objectArray[i].headline + '<br>' + 'SNIPPET: ' +  objectArray[i].snippet + '<br>' + 'PUBLICATION DATE: ' +  objectArray[i].publication_date;
      link.innerHTML = 'Click here for the article' + '<br>';
      link.setAttribute('href', objectArray[i].url);

    }
  }
  

http.onreadystatechange = function(){
  if (http.readyState === XMLHttpRequest.DONE) {
    console.log('done');
    if (http.status === 200) {
      console.log('status ok');
      var data = http.responseText;
      data = parser(data);
      data = arrangeData(data)
      applyToHtml(data);
      //console.log(data);
    } else {
      console.log('There was a problem with the request.');
    }
  }
}
