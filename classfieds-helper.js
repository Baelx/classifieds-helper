const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');
const config = require('./config.js');

function makeRequest(){

  //scraper API
  url: `http://api.scraperapi.com/?key=&url=${config.key}` + encodeURIComponent(siteSelection),

  axios.get(url)
      .then((response) => {
          if(response.status === 200) {
              const html = response.data;
              const $ = cheerio.load(html);
              let devtoList = [];
              $('.single-article').each(function(i, elem) {
                  devtoList[i] = {
                      title: $(this).find('h3').text().trim(),
                      url: $(this).children('.index-article-link').attr('href'),
                      tags: $(this).find('.tags').text().split('#')
                            .map(tag =>tag.trim())
                            .filter(function(n){ return n != "" })
                  }
              });
      }
  }, (error) => console.log(err) );
}

/*
User will be prompted to enter their location which will be saved in the DB.
Multiple locations will be a feature for later on.

Likely will need to build out an array of strings that correspond to a site's URL
representation of that city/location since each site does it differently.
For example, here are two test URL queries for CL and Kijiji, note the cities in the URLs:

kijiji: "https://www.kijiji.ca/b-victoria-bc/test/k0l1700173?dc=test"
craigslist: "https://victoria.craigslist.org/search/sss?query=test&sort=rel"
used: "https://www.usedvictoria.com/classifieds/all?description=test",

*/

function sitePicker() {
  // Capture input for which sites the user wants to query and write it to the DB

  return pickedSites;
}


function siteSelection() {
  // Query the DB for the site preferences of this user

  return seletion;
}

let sites = {
    craigslist: `https://${location}.craigslist.org/search/sss?query=${query}&sort=rel`,
    kijiji: `https://www.kijiji.ca/${location}/test/k0l1700173?dc=${query}`,
    used: `https://www.used${location}.com/classifieds/all?description=${query}`,
}
