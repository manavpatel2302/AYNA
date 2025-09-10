function doPost(e) {
  try {
    // Get the Google Sheet by ID
    var sheet = SpreadsheetApp.openById('1p91c-cnDk1F9eJtMu3bNZrc7h76775m8FOsi0VUBvqo').getActiveSheet();
    
    // Parse the JSON data from the request
    var data = JSON.parse(e.postData.contents);
    
    // If no data provided, try to get from parameters
    if (!data) {
      data = {
        timestamp: e.parameter.timestamp || new Date().toISOString(),
        name: e.parameter.name || '',
        email: e.parameter.email || '',
        message: e.parameter.message || ''
      };
    }
    
    // Add headers if the sheet is empty
    var lastRow = sheet.getLastRow();
    if (lastRow === 0) {
      sheet.appendRow(['Timestamp', 'Name', 'Email', 'Message']);
    }
    
    // Append the feedback data to the sheet
    sheet.appendRow([
      data.timestamp || new Date().toISOString(),
      data.name || '',
      data.email || '',
      data.message || ''
    ]);
    
    // Return success response
    return ContentService
      .createTextOutput(JSON.stringify({
        'success': true,
        'message': 'Data saved successfully'
      }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    // Return error response
    return ContentService
      .createTextOutput(JSON.stringify({
        'success': false,
        'error': error.toString()
      }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  // Handle GET requests (for testing)
  return ContentService
    .createTextOutput(JSON.stringify({
      'status': 'Google Apps Script is running',
      'message': 'Use POST to submit feedback data'
    }))
    .setMimeType(ContentService.MimeType.JSON);
}
