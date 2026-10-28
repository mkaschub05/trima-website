// Usage: socialcard <figure.png> <wordmark.png> <out.jpg>
// Builds the 1200×630 share image (Open Graph): Justitia on the right, wordmark and two lines on the left.
import AppKit

let a = CommandLine.arguments
let figure = NSImage(contentsOfFile: a[1])!
let word = NSImage(contentsOfFile: a[2])!
let W: CGFloat = 1200, H: CGFloat = 630

let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(W), pixelsHigh: Int(H), bitsPerSample: 8,
                           samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB,
                           bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
let ctx = NSGraphicsContext.current!.cgContext

// Background: the logo's near-black (the figure brings its own light).
NSColor(srgbRed: 8/255, green: 6/255, blue: 5/255, alpha: 1).setFill()
NSRect(x: 0, y: 0, width: W, height: H).fill()
// Figure on the right; its own dark background blends into the card. Soft fade on the left edge.
let fh: CGFloat = 600, fw = fh * figure.size.width / figure.size.height
let fx = W - fw + 40
figure.draw(in: NSRect(x: fx, y: (H - fh) / 2, width: fw, height: fh))
let fade = CGGradient(colorsSpace: CGColorSpaceCreateDeviceRGB(),
                      colors: [NSColor(srgbRed: 8/255, green: 6/255, blue: 5/255, alpha: 1).cgColor,
                               NSColor(srgbRed: 8/255, green: 6/255, blue: 5/255, alpha: 0).cgColor] as CFArray,
                      locations: [0, 1])!
ctx.drawLinearGradient(fade, start: CGPoint(x: fx, y: 0), end: CGPoint(x: fx + 330, y: 0), options: [])
// Fade top and bottom edges too.
ctx.drawLinearGradient(fade, start: CGPoint(x: 0, y: 0), end: CGPoint(x: 0, y: 60), options: [])
ctx.drawLinearGradient(fade, start: CGPoint(x: 0, y: H), end: CGPoint(x: 0, y: H - 60), options: [])

// Wordmark and text on the left.
let ww: CGFloat = 470, wh = ww * word.size.height / word.size.width
word.draw(in: NSRect(x: 80, y: 330, width: ww, height: wh))

let bronze = NSColor(srgbRed: 0.82, green: 0.6, blue: 0.42, alpha: 1)
let muted = NSColor(srgbRed: 0.66, green: 0.61, blue: 0.56, alpha: 1)
func draw(_ s: String, _ size: CGFloat, _ color: NSColor, _ kern: CGFloat, _ x: CGFloat, _ y: CGFloat, serif: Bool = false) {
    let font = serif ? (NSFont(name: "Iowan Old Style Bold", size: size) ?? NSFont.boldSystemFont(ofSize: size))
                     : NSFont.systemFont(ofSize: size, weight: .semibold)
    NSAttributedString(string: s, attributes: [.font: font, .foregroundColor: color, .kern: kern]).draw(at: NSPoint(x: x, y: y))
}
// Thin bronze rule, tagline, companies, domain.
bronze.setFill(); NSRect(x: 84, y: 300, width: 44, height: 1.5).fill()
draw("REAL SOLUTIONS", 17, bronze, 6, 144, 291)
draw("VIRENTIO  ·  LOCENTIO  ·  EXEMPTIO", 18, muted, 3, 84, 220)
draw("Dubai  ·  trima.ae", 18, muted, 2, 84, 186)

NSGraphicsContext.restoreGraphicsState()
let jpg = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.86])!
try! jpg.write(to: URL(fileURLWithPath: a[3]))
print("ok")
