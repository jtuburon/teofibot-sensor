Thermometer= function(){
    this.initThermo();
};

$.extend(Thermometer.prototype, {
	draw: 0,
	minTemp: 0,
	maxTemp: 50,
	minTempYPos: 300,
	maxTempYPos: 50,
	measureRect: null,

    initThermo: function(){
    	this.draw = SVG('thermometer').size(90, 370)
    	this.drawThermometer();
    	this.init_scale();
    },

    drawThermometer: function(){
		this.draw.rect(26, 320).move(17,30).attr({ fill: 'white', stroke : 'black', stroke_width : 3 })
		this.draw.circle(50).move(5,310).attr({ fill: 'white', stroke : 'black', stroke_width : 3 })	
		this.draw.rect(18, 20).move(21,300).attr({ fill: 'red'})
		this.draw.circle(42).move(9,314).attr({ fill: 'red'})	
	},

	draw_scale_measure: function(tempValue){
    	var yPos= this.minTempYPos - tempValue* this.unitSize;
		this.draw.line(38, yPos, 48, yPos).stroke({ width: 1 });
		this.draw.text(""+tempValue+"°C").move(50, yPos).font({ size: 10 })
	},

	init_scale: function(){
		this.unitSize= Math.abs(this.maxTempYPos- this.minTempYPos)/(this.maxTemp -this.minTemp)
		this.steps = 10 
		this.stepSize = (this.maxTemp -this.minTemp)/ this.steps
		for(step=0;step<=this.steps; step++){
			this.draw_scale_measure(step* this.stepSize);
		} 
	},

	plot_temperature: function(temperature){
		if(this.measureRect==null){
			this.measureRect= this.draw.rect(18, 0).move(21,0).attr({ fill: 'red'});
		}
		var yPos= this.minTempYPos - temperature * this.unitSize;
		this.measureRect.move(21, yPos)
		this.measureRect.size(18, temperature*this.unitSize);
	}
});

