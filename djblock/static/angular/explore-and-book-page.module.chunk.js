webpackJsonp(["explore-and-book-page.module"],{

/***/ "./src/app/save-page/explore-and-book-page/explore-and-book-page-routing.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return ExploreAndBookPageRoutingModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("./node_modules/@angular/core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_router__ = __webpack_require__("./node_modules/@angular/router/esm5/router.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__explore_and_book_page_component__ = __webpack_require__("./src/app/save-page/explore-and-book-page/explore-and-book-page.component.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var routes = [
    {
        path: '',
        component: __WEBPACK_IMPORTED_MODULE_2__explore_and_book_page_component__["a" /* ExploreAndBookPageComponent */]
    }
];
var ExploreAndBookPageRoutingModule = /** @class */ (function () {
    function ExploreAndBookPageRoutingModule() {
    }
    ExploreAndBookPageRoutingModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["K" /* NgModule */])({
            imports: [__WEBPACK_IMPORTED_MODULE_1__angular_router__["c" /* RouterModule */].forChild(routes)],
            exports: [__WEBPACK_IMPORTED_MODULE_1__angular_router__["c" /* RouterModule */]]
        })
    ], ExploreAndBookPageRoutingModule);
    return ExploreAndBookPageRoutingModule;
}());



/***/ }),

/***/ "./src/app/save-page/explore-and-book-page/explore-and-book-page.component.html":
/***/ (function(module, exports) {

module.exports = "<p>\n  explore-and-book-page works!\n</p>\n<h1>Project id is - {{project_id}}</h1>\n"

/***/ }),

/***/ "./src/app/save-page/explore-and-book-page/explore-and-book-page.component.scss":
/***/ (function(module, exports) {

module.exports = ""

/***/ }),

/***/ "./src/app/save-page/explore-and-book-page/explore-and-book-page.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return ExploreAndBookPageComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("./node_modules/@angular/core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_router__ = __webpack_require__("./node_modules/@angular/router/esm5/router.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var ExploreAndBookPageComponent = /** @class */ (function () {
    function ExploreAndBookPageComponent(route) {
        var _this = this;
        this.route = route;
        this.project_id = "";
        this.route.params.subscribe(function (params) {
            if (params['project_id']) {
                _this.project_id = params['project_id'];
            }
        });
    }
    ExploreAndBookPageComponent.prototype.ngOnInit = function () {
    };
    ExploreAndBookPageComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["n" /* Component */])({
            selector: 'app-explore-and-book-page',
            template: __webpack_require__("./src/app/save-page/explore-and-book-page/explore-and-book-page.component.html"),
            styles: [__webpack_require__("./src/app/save-page/explore-and-book-page/explore-and-book-page.component.scss")]
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__angular_router__["a" /* ActivatedRoute */]])
    ], ExploreAndBookPageComponent);
    return ExploreAndBookPageComponent;
}());



/***/ }),

/***/ "./src/app/save-page/explore-and-book-page/explore-and-book-page.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ExploreAndBookPageModule", function() { return ExploreAndBookPageModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("./node_modules/@angular/core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_common__ = __webpack_require__("./node_modules/@angular/common/esm5/common.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__explore_and_book_page_routing_module__ = __webpack_require__("./src/app/save-page/explore-and-book-page/explore-and-book-page-routing.module.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__explore_and_book_page_component__ = __webpack_require__("./src/app/save-page/explore-and-book-page/explore-and-book-page.component.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};




var ExploreAndBookPageModule = /** @class */ (function () {
    function ExploreAndBookPageModule() {
    }
    ExploreAndBookPageModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["K" /* NgModule */])({
            imports: [
                __WEBPACK_IMPORTED_MODULE_1__angular_common__["b" /* CommonModule */],
                __WEBPACK_IMPORTED_MODULE_2__explore_and_book_page_routing_module__["a" /* ExploreAndBookPageRoutingModule */]
            ],
            declarations: [__WEBPACK_IMPORTED_MODULE_3__explore_and_book_page_component__["a" /* ExploreAndBookPageComponent */]]
        })
    ], ExploreAndBookPageModule);
    return ExploreAndBookPageModule;
}());



/***/ })

});
//# sourceMappingURL=explore-and-book-page.module.chunk.js.map