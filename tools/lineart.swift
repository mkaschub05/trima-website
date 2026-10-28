// Usage: lineart <in> <out.png> <x> <y> <w> <h> <targetWidth> <edgeIntensity> <threshold> [noise sharpness contrast]
// Crops (top-left origin) and scales like sharpen.swift, then CILineOverlay turns the image into a sketch:
// black lines on transparent. The PNG is used as an alpha mask in CSS (lines get their colour there).
import Foundation
import CoreImage
import CoreImage.CIFilterBuiltins
import ImageIO
import UniformTypeIdentifiers

let a = CommandLine.arguments
let input = CIImage(contentsOf: URL(fileURLWithPath: a[1]))!
let (x, y, w, h) = (Double(a[3])!, Double(a[4])!, Double(a[5])!, Double(a[6])!)
let H = input.extent.height
var img = input.cropped(to: CGRect(x: x, y: H - y - h, width: w, height: h))
img = img.transformed(by: CGAffineTransform(translationX: -x, y: -(H - y - h)))

let scale = CIFilter.lanczosScaleTransform()
scale.inputImage = img
scale.scale = Float(Double(a[7])! / w)
img = scale.outputImage!

let lines = CIFilter.lineOverlay()
lines.inputImage = img
lines.edgeIntensity = Float(a[8])!
lines.threshold = Float(a[9])!
lines.nrNoiseLevel = a.count > 10 ? Float(a[10])! : 0.07
lines.nrSharpness = a.count > 11 ? Float(a[11])! : 0.71
lines.contrast = a.count > 12 ? Float(a[12])! : 50
img = lines.outputImage!.cropped(to: img.extent)

let ctx = CIContext()
let cg = ctx.createCGImage(img, from: img.extent)!
let dest = CGImageDestinationCreateWithURL(URL(fileURLWithPath: a[2]) as CFURL, UTType.png.identifier as CFString, 1, nil)!
CGImageDestinationAddImage(dest, cg, nil)
CGImageDestinationFinalize(dest)
print("\(cg.width)x\(cg.height)")
